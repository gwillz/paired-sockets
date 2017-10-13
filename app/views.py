import json, random, string, collections
from flask import redirect, render_template
from flask_socketio import join_room, send
from . import app, io

tokens = set()

@app.route('/<token>')
def subscriber(token):
    if token not in tokens:
        return redirect('/')
    return render_template('index.html', token='')


@app.route('/')
def producer():
    token = ''.join([string.hexdigits[round(random.random() * 16)] for _ in range(8)])
    tokens.add(token)
    return render_template('index.html', token=token)

@io.on('message')
def handle_json(message):
    if message['action'] == 'join':
        join_room(message['token'])
    
    elif message['action'] == 'data':
        send(message['data'], room=message['token'])
