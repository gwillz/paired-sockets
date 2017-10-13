from flask import redirect, render_template
from flask_socketio import join_room, send
from random_words import RandomWords
from . import app, io

tokens = set()
rw = RandomWords()

def gen_token():
    while True:
        token = '-'.join(rw.random_words(count=2))
        if len(token) < 12 and token not in tokens:
            tokens.add(token)
            return token

@app.route('/<token>')
def subscriber(token):
    if token not in tokens:
        return redirect('/')
    return render_template('index.html', token='')


@app.route('/')
def producer():
    token = gen_token()
    return render_template('index.html', token=token)

@io.on('message')
def handle_json(message):
    if message['action'] == 'join':
        join_room(message['token'])
    
    elif message['action'] == 'data':
        send(message['data'], room=message['token'])
