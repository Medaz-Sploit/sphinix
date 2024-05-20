Title: Dancing Machine
Date: 2024-05-19 19:10 
Category: HTB
Slug: dancing

# Dancing Machine
#HTB/STARTING_POINT


In this machine we learn to enumerate SMB file shares.

### To list shares 

```sh
kali@kali:~$ smbclient -L //<serverIP/name> -N
```

### To download all file to a backup file become handing when u have a large file system

```sh
kali@kali:~$ smbclient //<serverIP/name>/<shareDisk> -N -Tc backup.tar
```

