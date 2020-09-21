# Raspberry pi

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

1. Initial username and password are `pi`, `raspberry`.
2. Type `sudo passwd` and `passwd` to change password of super user and pi user.
3. Type `sudo apt-get update` and `sudo apt-get upgrade` to be up-to-date.
4. Type `sudo raspi-config` if you want to set another configurations like time zone.



## Auto reboot & run

1. Type `sudo crontab -e` and write `m h dom mon dow command` like `0 0 * * * /sbin/reboot`.

   ```shell
   pi@raspberrypi:~ $ sudo crontab -e
   no crontab for root - using an empty one
   crontab: installing new crontab
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