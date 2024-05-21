Title: Passive Enumeration
Date: 2024-05-09 02:09
Category: OSCP


### WHOIS Enumeration

```powershell
@kali:~$ whois megacorpone.com -h 192.168.50.251
Domain Name: MEGACORPONE.COM
Registry Domain ID: 1775445745_DOMAIN_COM-VRSN
Registrar WHOIS Server: whois.gandi.net
Registrar URL: http://www.gandi.net
Updated Date: 2019-01-01T09:45:03Z
Creation Date: 2013-01-22T23:01:00Z
Registry Expiry Date: 2023-01-22T23:01:00Z

@kali:~$ whois 38.100.193.70 -h 192.168.50.251
...
NetRange:
38.0.0.0 - 38.255.255.255
CIDR:
38.0.0.0/8
```

### Google Hacking

- site:megacorpone.com
- ext:php
- filetype:html
- intitle:"index of" "parent directory"
- https://www.exploit-db.com/google-hacking-database

### Netcraft

Let’s review some of Netcraft’s capabilities. For example, we can use Netcraft’s DNS search page
(https://searchdns.netcraft.com) to gather information about the megacorpone.com domain.

### Open-Source Code

This includes open-source projects and online code repositories such as GitHub, GitHub Gist, GitLab, and SourceForge

Once we’ve logged in to our Github account, we can search MegaCorp One’s repos for interesting
information. Let’s use filename:users to search for any files with the word “users” in the name.

For larger repos, we can use several tools to
help automate some of the searching, such as Gitrob and Gitleaks. Most of these tools
require an access tokento use the source code-hosting provider’s API.

> Tools that search through source code for secrets, like Gitrob or Gitleaks,
  generally rely on regular expressions or entropy233-based detections to identify
  potentially useful information. Entropy-based detection attempts to find strings
  that are randomly generated. The idea is that a long string of random characters
  and numbers is probably a password. No matter how a tool searches for secrets,
  no tool is perfect and they will miss things that a manual inspection might find.

### Shodan


-  hostname:megacorpone.com.
- port:"22"

### Security Headers and SSL/TLS

One such site, Security Headers will analyze HTTP response headers and provide basic
analysis of the target site’s security posture. We can use this to get an idea of an organization’s
coding and security practices based on the results.
Let’s scan www.megacorpone.com and check the results.
