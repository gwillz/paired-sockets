Watch Me Code!
==============

blah.

Install
-------
```sh
sudo apt-get install git python3 python3-pip

sudo mkdir -p /srv/paired
cd /srv/paired
sudo chown www-data: .

git clone https://git.mk2es.com/gwillz/paired-sockets .

sudo -u www-data -H pip3 install -r requirements.txt --user

sudo cp paired.service /etc/systemd/system
sudo ln -s nginx_paired.conf /etc/nginx/sites-enabled/paired

sudo systemctl daemon-reload
sudo systemctl start paired
sudo systemctl enable paired
sudo systemctl reload nginx
```
