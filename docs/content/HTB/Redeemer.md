Title : Redeemer Machine
Date  : 2024-05-19 19:10 
Category : HTB
Slug : redeemer


# Redeemer
#HTB/STARTING_POINT

This machine show you how to interact with a Redis server .


Doing Nmap scan show open port and specifically redid port open on :

```sh
kali@kali:~$ nmap -sC -sV -T4 -p- -oA nmap/Redeemer <serverIp>
```

Result :

```shell-session
# Nmap 7.93 scan initiated Thu Aug 24 02:07:23 2023 as: nmap -sC -sV -T4 -p- -oA nmap/Redeemer 10.129.6.102
Warning: 10.129.6.102 giving up on port because retransmission cap hit (6).
Nmap scan report for 10.129.6.102
Host is up (0.11s latency).
Not shown: 65526 closed tcp ports (conn-refused)
PORT      STATE    SERVICE VERSION
6379/tcp  open     redis   Redis key-value store 5.0.7
23201/tcp filtered unknown
23819/tcp filtered unknown
25153/tcp filtered unknown
34008/tcp filtered unknown
35903/tcp filtered unknown
39049/tcp filtered unknown
40140/tcp filtered unknown
47535/tcp filtered unknown

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Thu Aug 24 02:25:02 2023 -- 1 IP address (1 host up) scanned in 1059.07 seconds

```

Connect to redis ;
```sh
kali@kali:~$ redis-cli -h <hostname/ip>
```

Get all db ;
```sh
redis-cli> config get databases
```

Get existed keys with correspond db index;
```sh
redis-cli> info keyspace 
```

Select desired db;
```sh
redis-cli> select <N>
```

Get info on Redis server;
```sh
redis-cli> info
```

Dump all keys;
```sh
redis-cli> keys *
```

Get random keys;
```sh
redis-cli> randomkey 
```

Print specified key value;
```sh
redis-cli> get <keyname>
```
