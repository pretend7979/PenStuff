# PenStuff

A personal reference collection of web application security payloads, bypasses, and penetration testing resources.

> **For authorized security testing and educational purposes only.**

---

## Structure

Each vulnerability category follows a consistent layout:

| Item | Description |
|------|-------------|
| `README.md` | Vulnerability overview, exploitation techniques, and payloads |
| `Intruder/` | Wordlists and payload files for Burp Suite Intruder |
| `Images/` | Supporting screenshots for the README |
| `Files/` | Auxiliary files referenced in the README |

Use the [`_template_vuln/`](_template_vuln/) folder as a starting point when adding a new category.

---

## Vulnerability Categories

| Category | Description |
|----------|-------------|
| [Account Takeover](Account%20Takeover/) | ATO techniques and bypass methods |
| [API Key Leaks](API%20Key%20Leaks/) | Discovering and exploiting exposed API keys |
| [AWS / S3 Buckets](AWS%20Amazon%20Bucket%20S3/) | Cloud misconfiguration and bucket enumeration |
| [Command Injection](Command%20Injection/) | OS command injection payloads and techniques |
| [CORS Misconfiguration](CORS%20Misconfiguration/) | Cross-origin resource sharing exploits |
| [CRLF Injection](CRLF%20Injection/) | Carriage return / line feed injection |
| [CSRF Injection](CSRF%20Injection/) | Cross-site request forgery |
| [CSV Injection](CSV%20Injection/) | Formula injection in exported data |
| [CVE Exploits](CVE%20Exploits/) | Standalone exploit scripts for known CVEs |
| [Directory Traversal](Directory%20Traversal/) | Path traversal and file disclosure |
| [File Inclusion](File%20Inclusion/) | LFI / RFI payloads |
| [GraphQL Injection](GraphQL%20Injection/) | Introspection abuse and injection techniques |
| [Insecure Deserialization](Insecure%20Deserialization/) | Java, PHP, Python, Ruby deserialization |
| [Insecure Direct Object References](Insecure%20Direct%20Object%20References/) | IDOR exploitation patterns |
| [Insecure Management Interface](Insecure%20Management%20Interface/) | Exposed admin panels and management endpoints |
| [Insecure Source Code Management](Insecure%20Source%20Code%20Management/) | .git/.svn exposure and extraction |
| [JSON Web Token](JSON%20Web%20Token/) | JWT attacks — alg:none, secret cracking, key confusion |
| [Kubernetes](Kubernetes/) | K8s misconfigurations and cluster attacks |
| [LaTeX Injection](LaTeX%20Injection/) | Injection via LaTeX rendering engines |
| [LDAP Injection](LDAP%20Injection/) | LDAP filter bypass and blind injection |
| [NoSQL Injection](NoSQL%20Injection/) | MongoDB and other NoSQL injection |
| [OAuth](OAuth/) | OAuth flow abuse and token theft |
| [Open Redirect](Open%20Redirect/) | URL redirection bypasses |
| [Race Condition](Race%20Condition/) | TOCTOU and concurrent request attacks |
| [Request Smuggling](Request%20Smuggling/) | HTTP/1.1 and HTTP/2 desync attacks |
| [SAML Injection](SAML%20Injection/) | XML signature wrapping and SAML bypass |
| [Server Side Request Forgery](Server%20Side%20Request%20Forgery/) | SSRF payloads and cloud metadata abuse |
| [Server Side Template Injection](Server%20Side%20Template%20Injection/) | SSTI payloads across Jinja2, Twig, Freemarker, etc. |
| [SQL Injection](SQL%20Injection/) | Error-based, blind, and time-based SQLi |
| [Tabnabbing](Tabnabbing/) | Reverse tabnabbing via target=_blank |
| [Type Juggling](Type%20Juggling/) | PHP loose comparison exploits |
| [Upload Insecure Files](Upload%20Insecure%20Files/) | Bypassing file upload filters |
| [Web Cache Deception](Web%20Cache%20Deception/) | Cache poisoning and deception |
| [Web Sockets](Web%20Sockets/) | WebSocket hijacking and injection |
| [XPATH Injection](XPATH%20Injection/) | Blind and error-based XPath injection |
| [XSLT Injection](XSLT%20Injection/) | XSLT server-side injection |
| [XSS Injection](XSS%20Injection/) | Reflected, stored, DOM-based, and filter bypasses |
| [XXE Injection](XXE%20Injection/) | XML external entity attacks |

---

## Methodology & Resources

General pentest methodology, cheat sheets, and post-exploitation notes:

- [Methodology and enumeration](Methodology%20and%20Resources/Methodology%20and%20enumeration.md)
- [Active Directory Attack](Methodology%20and%20Resources/Active%20Directory%20Attack.md)
- [Cloud - AWS Pentest](Methodology%20and%20Resources/Cloud%20-%20AWS%20Pentest.md)
- [Cloud - Azure Pentest](Methodology%20and%20Resources/Cloud%20-%20Azure%20Pentest.md)
- [Cobalt Strike - Cheatsheet](Methodology%20and%20Resources/Cobalt%20Strike%20-%20Cheatsheet.md)
- [Container - Docker Pentest](Methodology%20and%20Resources/Container%20-%20Docker%20Pentest.md)
- [Linux - Persistence](Methodology%20and%20Resources/Linux%20-%20Persistence.md)
- [Linux - Privilege Escalation](Methodology%20and%20Resources/Linux%20-%20Privilege%20Escalation.md)
- [Metasploit - Cheatsheet](Methodology%20and%20Resources/Metasploit%20-%20Cheatsheet.md)
- [Miscellaneous - Tricks](Methodology%20and%20Resources/Miscellaneous%20-%20Tricks.md)
- [Network Discovery](Methodology%20and%20Resources/Network%20Discovery.md)
- [Network Pivoting Techniques](Methodology%20and%20Resources/Network%20Pivoting%20Techniques.md)
- [Reverse Shell Cheatsheet](Methodology%20and%20Resources/Reverse%20Shell%20Cheatsheet.md)
- [Bind Shell Cheatsheet](Methodology%20and%20Resources/Bind%20Shell%20Cheatsheet.md)
- [Subdomains Enumeration](Methodology%20and%20Resources/Subdomains%20Enumeration.md)
- [Windows - Download and Execute](Methodology%20and%20Resources/Windows%20-%20Download%20and%20Execute.md)
- [Windows - Mimikatz](Methodology%20and%20Resources/Windows%20-%20Mimikatz.md)
- [Windows - Persistence](Methodology%20and%20Resources/Windows%20-%20Persistence.md)
- [Windows - Post Exploitation Koadic](Methodology%20and%20Resources/Windows%20-%20Post%20Exploitation%20Koadic.md)
- [Windows - Privilege Escalation](Methodology%20and%20Resources/Windows%20-%20Privilege%20Escalation.md)
- [Windows - Using credentials](Methodology%20and%20Resources/Windows%20-%20Using%20credentials.md)

---

## Additional Resources

- [Books](BOOKS.md) — recommended reading list
- [YouTube](YOUTUBE.md) — channels and conference talks
