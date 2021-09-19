# Raspberry pi 3(Raspbian)

## Installation

1. [Download](https://www.raspberrypi.org/downloads/) raspberry pi's os.

2. Use [Win32 Disk Imager](https://sourceforge.net/projects/win32diskimager/) or [balenaEtcher](https://www.balena.io/etcher/) to install os at sd card.

3. Make a file named `ssh` to activate ssh.

4. Make a file named `wpa_supplicant.conf` and write a wifi information like below.

   ```
   ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
   network={
       ssid="wifi name"
       psk="wifi password"
       key_mgmt=WPA-PSK
   }
   ```

## Configuration

### basic

1. Initial username and password are `pi`, `raspberry`.
2. Type `sudo passwd` and `passwd` to change password of super user and pi user.
3. Type `sudo apt-get update` and `sudo apt-get upgrade` to be up-to-date.
4. Type `sudo raspi-config` if you want to set another configurations like time zone.

### swap-memory

```bash
$ sudo /etc/init.d/dphys-swapfile stop
$ sudo vi /etc/dphys-swapfile
```

```
# /etc/dphys-swapfile
...
CONF_SWAPSIZE=2048
...
```

```bash
$ sudo /etc/init.d/dphys-swapfile start
$ free -h
```

## Auto reboot & run

1. Type `sudo crontab -e` and write `m h dom mon dow command` like `0 0 * * * /sbin/reboot`.

   ```shell
   $ sudo crontab -e
   no crontab for root - using an empty one
   crontab: installing new crontab
   $ service cron restart
   ```

2. Can check whether reboot is done or not by typing `journalctl -b`.

3. Type `sudo nano /etc/profile` and add commands you want to run when system is started.

4. Type `sudo raspi-config` and select `Boot Options` then `Desktop/CLI` then `Console Autologin`.

## Python

### Configure basic python

Make a new symbolic link at /usr/bin/

$ `sudo ln -sf /usr/bin/python3 /user/bin/python`

`s`: symbolic

`f`: force

cf. `unlink symbolic_name`

### [Version update](https://www.python.org/downloads/source/)

$ `wget download_url`

$ `tar xvfz Python-x.x.x.tgz `

$ `cd Python-x.x.x`

$ `./configure`

$ `make`

$ `sudo make install`

### Pip

$ `sudo apt-get install python3-pip`

### [Deadsnakes](https://launchpad.net/~deadsnakes/+archive/ubuntu/ppa)(Ubuntu)

```bash
$ sudo add-apt-repository ppa:deadsnakes/ppa
$ sudo apt-get update
$ sudo apt install python3.7
```

### alias

```bash
$ sudo nano ~/.bashrc
```

```
-------default-------
alias python='python3.7'
```

## Samba

### Installation

$ `sudo apt-get install samba samba-common-bin`

$ `sudo nano /etc/samba/smb.conf`

```
[id]
   path = folder_path
   writeable=Yes
   create mask=0777
   directory mask=0777
   public=no
```

$ `sudo smbpasswd -a {id}`

$ `sudo systemctl restart smbd`

## Docker

### Docker Installation (Rpi3 raspbian buster)

```bash
$ curl -fsSL https://get.docker.com -o get-docker.sh
$ sudo sh get-docker.sh
$ sudo usermod -aG docker pi
$ newgrp docker
$ docker run hello-world
```

### Docker Compose Installation (Rpi3 raspbian buster)

```bash
$ sudo apt-get install libffi-dev libssl-dev -y
$ sudo apt install python3-dev -y
$ sudo apt-get install -y python3 python3-pip -y
$ sudo pip3 install docker-compose
$ docker-compose -v
```

## CUPS

> Common Unix Printing System

```bash
$ sudo apt install cups
$ sudo apt install printer-driver-all
$ sudo usermod -a -G lpadmin pi
$ sudo cupsctl --remote-any
$ sudo /etc/init.d/cups restart
```

http://raspberrypi-ip:631

![image-20210902214343699](https://raw.githubusercontent.com/powerticket/typora-image-repo/image/img/image-20210902214343699.png)

![image-20210919130315776](https://raw.githubusercontent.com/powerticket/typora-image-repo/image/img/image-20210919130315776.png)

```bash
$ lp /usr/share/cups/data/testprint
```

## Auto-Login

```bash
 $ ssh-keygen -t rsa
Generating public/private rsa key pair.
Enter file in which to save the key (/home/pi/.ssh/id_rsa):
Created directory '/home/pi/.ssh'.
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
Your identification has been saved in /home/pi/.ssh/id_rsa.
Your public key has been saved in /home/pi/.ssh/id_rsa.pub.
The key fingerprint is:
# key generated
$ cp ~/.ssh/id_rsa.pub ~/.ssh/authorized_keys
```

puttygen -> Load `~/.ssh/id_rsa` file -> Save private key

![image-20210903210317429](https://raw.githubusercontent.com/powerticket/typora-image-repo/image/img/image-20210903210317429.png)

putty -> SSH -> Auth -> Private key file for authentication

![image-20210903210419070](https://raw.githubusercontent.com/powerticket/typora-image-repo/image/img/image-20210903210419070.png)

