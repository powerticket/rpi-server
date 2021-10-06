#!/bin/bash

echo "apt update && upgrade"
sudo apt update && sudo apt upgrade -y

echo "install cups"
sudo apt install cups printer-driver-all -y
sudo usermod -a -G lpadmin pi
sudo cupsctl --remote-any
sudo /etc/init.d/cups restart

echo "samba install"
mkdir samba
sudo apt install samba samba-common-bin -y
sudo echo "[pi]
   path=/home/pi/samba
   writeable=Yes
   create mask=0777
   directory mask=0777
   public=no" >> /etc/samba/smb.conf
sudo smbpasswd -a pi
sudo systemctl restart smbd

echo "auto-login"
ssh-keygen -t rsa
sudo cp ~/.ssh/id_rsa.pub ~/.ssh/authorized_keys
sudo cp ~/.ssh/id_rsa ~/samba/id_rsa

echo "reboot"
sudo reboot
