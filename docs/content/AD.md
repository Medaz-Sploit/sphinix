Title: Active Enumeration
Date: 2024-05-08 21:00
Category: OSCP

	
### DNS Enumeration

- **NS**: Nameserver records contain the name of the authoritative servers hosting the DNS records for a domain.
- **A**: Also known as a host record, the “a record” contains the IPv4 address of a hostname (such as www.megacorpone.com)
- **AAAA**: Also known as a quad A host record, the “aaaa record” contains the IPv6 address of a hostname (such as www.megacorpone.com).
- **MX**: Mail Exchange records contain the names of the servers responsible for handling email for the domain. A domain can contain multiple MX records.
- **PTR**: Pointer Records are used in reverse lookup zones and can find the records associated with an IP address.
- **CNAME**: Canonical Name Records are used to create aliases for other host records.
- **TXT**: Text records can contain any arbitrary data and be used for various purposes, such as domain ownership verification.

```powershell
@kali:~$ host www.megacorpone.com
www.megacorpone.com has address 149.56.244.87

@kali:~$ host -t mx megacorpone.com
megacorpone.com mail is handled by 10 fb.mail.gandi.net.
megacorpone.com mail is handled by 20 spool.mail.gandi.net.
megacorpone.com mail is handled by 50 mail.megacorpone.com.
megacorpone.com mail is handled by 60 mail2.megacorpone.com.

@kali:~$ host -t txt megacorpone.com
megacorpone.com descriptive text "Try Harder"
megacorpone.com descriptive text "google-site-
verification=U7B_b0HNeBtY4qYGQZNsEYXfCJ32hMNV3GtC0wWq5pA"

@kali:~$ host www.megacorpone.com
www.megacorpone.com has address 149.56.244.87

@kali:~$ host idontexist.megacorpone.com
Host idontexist.megacorpone.com not found: 3(NXDOMAIN)
```

```powershell
@kali:~$ dig @nagoya.nagoya-industries.com nagoya-industries.com +tcp
```

```powershell
@kali:~$ cat list.txt
www
ftp
mail
owa
proxy
router

@kali:~$ for ip in $(cat list.txt); do host $ip.megacorpone.com; done
www.megacorpone.com has address 149.56.244.87
Host ftp.megacorpone.com not found: 3(NXDOMAIN)
mail.megacorpone.com has address 51.222.169.212
Host owa.megacorpone.com not found: 3(NXDOMAIN)
Host proxy.megacorpone.com not found: 3(NXDOMAIN)
router.megacorpone.com has address 51.222.169.214
```

```powershell
@kali:~$ wfuzz -w /usr/share/wordlists/dnsmap.txt -u http://devvortex.htb -H 'Host: FUZZ.devvortex.htb' -t 50 --hc 302

********************************************************
* Wfuzz 3.1.0 - The Web Fuzzer                         *
********************************************************

Target: http://devvortex.htb/
Total requests: 17576

=====================================================================
ID           Response   Lines    Word       Chars       Payload                     
=====================================================================

000002154:   200        501 L    1581 W     23221 Ch    "dev"

```

```powershell
@kali:~$ gobuster vhost -u devvortex.htb -w /usr/share/wordlists/dnsmap.txt


```

```powershell
@kali:~$ for ip in $(seq 200 254); do host 51.222.169.$ip; done | grep -v "not
found"
...
208.169.222.51.in-addr.arpa domain name pointer admin.megacorpone.com.
209.169.222.51.in-addr.arpa domain name pointer beta.megacorpone.com.
210.169.222.51.in-addr.arpa domain name pointer fs1.megacorpone.com.
211.169.222.51.in-addr.arpa domain name pointer intranet.megacorpone.com.
212.169.222.51.in-addr.arpa domain name pointer mail.megacorpone.com.
213.169.222.51.in-addr.arpa domain name pointer mail2.megacorpone.com.
214.169.222.51.in-addr.arpa domain name pointer router.megacorpone.com.
215.169.222.51.in-addr.arpa domain name pointer siem.megacorpone.com.
216.169.222.51.in-addr.arpa domain name pointer snmp.megacorpone.com.
217.169.222.51.in-addr.arpa domain name pointer syslog.megacorpone.com.
218.169.222.51.in-addr.arpa domain name pointer support.megacorpone.com.
219.169.222.51.in-addr.arpa domain name pointer test.megacorpone.com.
220.169.222.51.in-addr.arpa domain name pointer vpn.megacorpone.com.
```

```powershell
@kali:~$ dnsrecon -d megacorpone.com -t std
[*] std: Performing General Enumeration against: megacorpone.com...
[-] DNSSEC is not configured for megacorpone.com
[*] SOA ns1.megacorpone.com 51.79.37.18
[*] NS ns1.megacorpone.com 51.79.37.18
[*] NS ns3.megacorpone.com 66.70.207.180
[*] NS ns2.megacorpone.com 51.222.39.63
[*] MX mail.megacorpone.com 51.222.169.212
[*] MX spool.mail.gandi.net 217.70.178.1
[*] MX fb.mail.gandi.net 217.70.178.217
[*] MX fb.mail.gandi.net 217.70.178.216
[*] MX fb.mail.gandi.net 217.70.178.215
[*] MX mail2.megacorpone.com 51.222.169.213
[*] TXT megacorpone.com Try Harder
[*] TXT megacorpone.com google-site-
verification=U7B_b0HNeBtY4qYGQZNsEYXfCJ32hMNV3GtC0wWq5pA
[*] Enumerating SRV Records
[+] 0 Records Found
```

```powershell
@kali:~$ cat list.txt
www
ftp
mail
owa
proxy
router

@kali:~$ dnsrecon -d megacorpone.com -D ~/list.txt -t brt
[*] Using the dictionary file: /home/kali/list.txt (provided by user)
[*] brt: Performing host and subdomain brute force against megacorpone.com...
[+]   A www.megacorpone.com 149.56.244.87
[+]   A mail.megacorpone.com 51.222.169.212
[+]   A router.megacorpone.com 51.222.169.214
[+] 3 Records Found
```

```powershell
@kali:~$ dnsenum megacorpone.com
...
dnsenum VERSION:1.2.6
----- megacorpone.com -----
...
Brute forcing with /usr/share/dnsenum/dns.txt:
_______________________________________________
admin.megacorpone.com.   5     IN       A              51.222.169.208
```

```powershell
C:\Users\student> nslookup mail.megacorptwo.com
DNS request timed out.
timeout was 2 seconds.
Server: UnKnown
Address: 192.168.50.151
```

```powershell
C:\Users\student>nslookup -type=TXT info.megacorptwo.com 192.168.50.151
Server: UnKnown
Address: 192.168.50.151
info.megacorptwo.com
text =
"greetings from the TXT record body"
```

### TC/UDP Scanning

```powershell
@kali:~$ nc -nvv -w 1 -z 192.168.50.152 3388-3390
(UNKNOWN) [192.168.50.152] 3390 (?) : Connection refused
(UNKNOWN) [192.168.50.152] 3389 (ms-wbt-server) open
(UNKNOWN) [192.168.50.152] 3388 (?) : Connection refused
sent 0, rcvd 0
```
![[Pasted image 20240202113027.png]]

```powershell
@kali:~$ nc -nv -u -z -w 1 192.168.50.149 120-123
(UNKNOWN) [192.168.50.149] 123 (ntp) open
```
![[Pasted image 20240202113105.png]]

### Port Scanning with Nmap

```powershell
@kali:~$ sudo iptables -I INPUT 1 -s 192.168.50.149 -j ACCEPT

@kali:~$ sudo iptables -I OUTPUT 1 -d 192.168.50.149 -j ACCEPT

@kali:~$ sudo iptables -Z

@kali:~$ nmap 192.168.50.149

@kali:~$ sudo iptables -vn -L

@kali:~$ sudo iptables -Z

@kali:~$ nmap -p 1-65535 192.168.50.149

@kali:~$ sudo iptables -vn -L
```

```powershell
@kali:~$ sudo nmap -sS 192.168.50.149

@kali:~$ nmap -sT 192.168.50.149

@kali:~$ sudo nmap -sU 192.168.50.149

@kali:~$ sudo nmap -sU -sS 192.168.50.149

@kali:~$ nmap -sn 192.168.50.1-253

@kali:~$ nmap -v -sn 192.168.50.1-253 -oG ping-sweep.txt

@kali:~$ grep Up ping-sweep.txt | cut -d " " -f 2

@kali:~$ nmap -p 80 192.168.50.1-253 -oG web-sweep.txt

@kali:~$ grep open web-sweep.txt | cut -d" " -f2

@kali:~$ nmap -sT -A --top-ports=20 192.168.50.1-253 -oG top-port-sweep.txt

@kali:~$ cat /usr/share/nmap/nmap-services

@kali:~$ sudo nmap -O 192.168.50.14 --osscan-guess

@kali:~$ nmap -sT -A 192.168.50.14

@kali:~$ nmap --script http-headers 192.168.50.6

@kali:~$ nmap --script-help http-headers
```

```powershell
PS C:\Users\student> Test-NetConnection -Port 445 192.168.50.151
ComputerName : 192.168.50.151
RemoteAddress : 192.168.50.151
RemotePort : 445
InterfaceAlias : Ethernet0
SourceAddress : 192.168.50.152
TcpTestSucceeded : True
```

```powershell
PS C:\Users\student> 1..1024 | % {echo ((New-Object
Net.Sockets.TcpClient).Connect("192.168.50.151", $_)) "TCP port $_ is open"} 2>$null
TCP port 88 is open
```

### SMB Enumeration

```powershell
@kali:~$ nmap -v -p 139,445 -oG smb.txt 192.168.50.1-254

@kali:~$ cat smb.txt

@kali:~$ sudo nbtscan -r 192.168.50.0/24

@kali:~$ ls -1 /usr/share/nmap/scripts/smb*

@kali:~$ ls -1 /usr/share/nmap/scripts/smb*

@kali:~$ nmap -v -p 139,445 --script smb-os-discovery 192.168.50.152
```

```powershell
C:\Users\student>net view \\dc01 /all
```

### SMTP Enumeration

```powershell
@kali:~$ nc -nv 192.168.50.8 25
(UNKNOWN) [192.168.50.8] 25 (smtp) open
220 mail ESMTP Postfix (Ubuntu)
VRFY root
252 2.0.0 root
VRFY idontexist
```

```python
#!/usr/bin/python
import socket
import sys
if len(sys.argv) != 3:
print("Usage: vrfy.py <username> <target_ip>")
sys.exit(0)
# Create a Socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connect to the Server
ip = sys.argv[2]
connect = s.connect((ip,25))
# Receive the banner
banner = s.recv(1024)
print(banner)
# VRFY a user
user = (sys.argv[1]).encode()
s.send(b'VRFY ' + user + b'\r\n')
result = s.recv(1024)
print(result)
# Close the socket
s.close()
```

```powershell
@kali:~/Desktop$ python3 smtp.py root 192.168.50.8
b'220 mail ESMTP Postfix (Ubuntu)\r\n'
b'252 2.0.0 root\r\n'

@kali:~/Desktop$ python3 smtp.py johndoe 192.168.50.8
b'220 mail ESMTP Postfix (Ubuntu)\r\n'
b'550 5.1.1 <johndoe>: Recipient address rejected: User unknown in local recipient
table\r\n'
```

```powershell
PS C:\Users\student> Test-NetConnection -Port 25 192.168.50.8
ComputerName : 192.168.50.8 
RemoteAddress : 192.168.50.8
RemotePort : 25
InterfaceAlias : Ethernet0
SourceAddress : 192.168.50.152
TcpTestSucceeded : True

PS C:\Windows\system32> dism /online /Enable-Feature /FeatureName:TelnetClient

C:\Windows\system32>telnet 192.168.50.8 25
220 mail ESMTP Postfix (Ubuntu)
VRFY goofy
550 5.1.1 <goofy>: Recipient address rejected: User unknown in local recipient table
VRFY root
252 2.0.0 root
```

### SNMP Enumeration

| Code | Description |
| ---- | ---- |
| 1.3.6.1.2.1.25.1.6.0 | System Processes |
| 1.3.6.1.2.1.25.4.2.1.2 | Running Programs |
| 1.3.6.1.2.1.25.4.2.1.4 | Processes Path |
| 1.3.6.1.2.1.25.2.3.1.4 | Storage Units |
| 1.3.6.1.2.1.25.6.3.1.2 | Software Name |
| 1.3.6.1.4.1.77.1.2.25 | User Accounts |
| 1.3.6.1.2.1.6.13.1.3 | TCP Local Ports |
```powershell
@kali:~$ sudo nmap -sU --open -p 161 192.168.50.1-254 -oG open-snmp.txt

@kali:~$ echo public > community
@kali:~$ echo private >> community
@kali:~$ echo manager >> community

@kali:~$ for ip in $(seq 1 254); do echo 192.168.50.$ip; done > ips

@kali:~$ onesixtyone -c community -i ips
```

```powershell
@kali:~$ snmpwalk -c public -v1 -t 10 192.168.50.151

@kali:~$ snmpwalk -c public -v1 192.168.50.151 1.3.6.1.4.1.77.1.2.25

@kali:~$ snmpwalk -c public -v1 192.168.50.151 1.3.6.1.2.1.25.4.2.1.2

@kali:~$ snmpwalk -c public -v1 192.168.50.151 1.3.6.1.2.1.25.6.3.1.2

@kali:~$ snmpwalk -c public -v1 192.168.50.151 1.3.6.1.2.1.6.13.1.3
```
