## Raspberry pi 4(Ubuntu Server)

### [Installation](https://ubuntu.com/tutorials/how-to-install-ubuntu-on-your-raspberry-pi#1-overview)

[Raspberry Pi Imager for Windows](https://downloads.raspberrypi.org/imager/imager_latest.exe)

![Screenshot from 2021-04-28 11-15-19](https://ubuntucommunity.s3.dualstack.us-east-2.amazonaws.com/optimized/2X/1/1443a1624b2c3e4f48bc2ec18dbadbdfb052f636_2_690x464.png)

`network-config`

```
wifis:
  wlan0:
    dhcp4: true
    optional: true
    access-points:
      "<wifi network name>":
        password: "<wifi password>"
```

### Timezone Configuration

`$ sudo dpkg-reconfigure tzdata`

![image-20210911223629351](https://raw.githubusercontent.com/powerticket/typora-image-repo/image/img/image-20210911223629351.png)

### Docker

#### [Installation](https://docs.docker.com/engine/install/ubuntu/)

```bash
$ sudo apt update
$ sudo apt install apt-transport-https ca-certificates curl gnupg lsb-release
$ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
$ echo \
  "deb [arch=arm64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
$ sudo apt update
$ sudo apt install docker-ce docker-ce-cli containerd.io
$ sudo docker run hello-world
$ sudo groupadd docker
$ sudo usermod -aG docker $USER
$ newgrp docker
$ docker run hello-world
```

