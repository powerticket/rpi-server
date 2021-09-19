## Monitoring

![image-20210919131023605](https://raw.githubusercontent.com/powerticket/typora-image-repo/image/img/image-20210919131023605.png)

### Docker Compose

```yaml
version: "3"
services:
  grafana:
    image: grafana/grafana
    container_name: grafana
    restart: always
    ports:
      - 3000:3000
  influxdb:
    image: influxdb:1.8
    container_name: influxdb
    restart: always
    ports:
      - 8086:8086
  telegraf:
    image: telegraf
    container_name: telegraf
    restart: always
    environment:
      HOST_PROC: /rootfs/proc
      HOST_SYS: /rootfs/sys
      HOST_ETC: /rootfs/etc
    volumes:
     - ./telegraf.conf:/etc/telegraf/telegraf.conf:ro
     - /var/run/docker.sock:/var/run/docker.sock:ro
     - /sys:/rootfs/sys:ro
     - /proc:/rootfs/proc:ro
     - /etc:/rootfs/etc:ro
```

### Reference

https://grafana.com/grafana/dashboards/10578

https://dev.to/project42/install-grafana-influxdb-telegraf-using-docker-compose-56e9

https://www.youtube.com/watch?v=LB9l9YngfsI