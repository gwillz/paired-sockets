Watch Me Code!
==============

blah.

Install
-------
```sh
sudo apt-get install git python3 python3-pip python3-gunicorn

sudo mkdir /srv/paired
sudo chown www-data: /srv/paired

git clone https://git.mk2es.com/gwillz/paired-sockets /srv/paired

sudo -u www-data -H pip3 install flask flask-socketio gevent gevent-websocket --user

sudo cp /srv/paired/paired.service /etc/systemd/system
sudo ln -s /srv/paired/nginx_paired.conf /etc/nginx/sites-enabled/paired

sudo systemctl daemon-reload
sudo systemctl start paired
sudo systemctl enable paired
```
