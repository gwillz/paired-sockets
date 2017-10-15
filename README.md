Watch Me Code!
==============
Live code sharing!

Scrapped together with Flask, Socket.io, and Bulma styles.

Don't expect things to be considered properly, it fundamentally works and that's
all it needs to do.

A live version can be seen at [paired.gwillz.com](//paired.gwillz.com).

But please don't DDoS me. There's no diffing for the code/data, so I can imagine traffic being quite ugly if it picked up.


Known bugs/todos
----------------
- a new watcher will see nothing until the host writes new code
  - will require a server-side store of code/text
  - or a 'request' packet whenever a watcher joins to trigger the host to send
  - `#ugh`
- text highlighting
  - will likely require ace or codemirror. yay.
  - dynamic loading of language styles or just everything at once?
  - `#bloat`
- cannot resume/restore code if session is closed
  - potentially solved if storing code server-side
  - `#featurecreep`
- only send diffs of code
  - would also require server-side code or a 'request' packet
  - `#prematureoptimization`


Install
-------
```sh
sudo apt-get install git python3 python3-pip

sudo mkdir -p /srv/paired
cd /srv/paired
sudo chown www-data: .

git clone https://github.com/gwillz/paired-sockets .

sudo -u www-data -H pip3 install -r requirements.txt --user

sudo cp paired.service /etc/systemd/system
sudo ln -s nginx_paired.conf /etc/nginx/sites-enabled/paired

sudo systemctl daemon-reload
sudo systemctl start paired
sudo systemctl enable paired
sudo systemctl reload nginx
```
