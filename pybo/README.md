# Pybo Challenge

> 파이보는 파이썬 Django 웹 프레임워크로 만들어진 웹 사이트로 회원간 질문, 답변, 댓글 기능을 사용할 수 있다.



###### Flick through



## [Django](https://www.djangoproject.com/)

> Web framework



### Project tree



### Settings

```python
# settings.py

ALLOWED_HOSTS = ['jwp0530.iptime.org']
```



### App

#### pybo

#### accounts



## [PostgreSQL](https://www.postgresql.org/)

> Database





## [NGINX](https://www.nginx.com/)

> Web server



### Installation

```bash
$ sudo apt install nginx
```



### Launch

```bash
$ sudo systemctl start nginx
```



## [Gunicorn](https://gunicorn.org/)

> WSGI server



### Installation

```bash
$ pip install gunicorn
```



### Launch

```python
# myapp.py

def app(environ, start_response):
        data = b"Hello, World!\n"
        start_response("200 OK", [
            ("Content-Type", "text/plain"),
            ("Content-Length", str(len(data)))
        ])
        return iter([data])
```

```bash
$ gunicorn -w 4 myapp:app
```

```bash
$ gunicorn --bind 0.0.0.0 pybo.wsgi
```

```bash
$ gunicorn -w 2 --forwarded-allow-ips="jwp0530.iptime.org" pybo.wsgi
```



### Add as a service

```bash
$ sudo nano /etc/systemd/system/gunicorn.service
```

```
[Unit]
Description=gunicorn daemon
After=network.target

[Service]
User=pi
Group=pi
WorkingDirectory=/home/pi/rpi-server/pybo
ExecStart=/home/pi/rpi-server/pybo/venv/bin/gunicorn \
        --workers 2 \
        --bind unix:/tmp/gunicorn.sock \
        pybo.wsgi
[Install]
WantedBy=multi-user.target

```

```bash
$ sudo systemctl enable gunicorn.service
$ sudo systemctl start gunicorn.service
```



## Domain name



## Security

### Http

https://www.youtube.com/watch?v=LoYpXoBJPMc&list=PLRx0vPvlEmdChjc6N3JnLaX-Gihh5pHcx&index=2&ab_channel=%EB%8F%99%EB%B9%88%EB%82%98