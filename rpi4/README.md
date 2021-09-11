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
