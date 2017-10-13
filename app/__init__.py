from flask import Flask
from flask_socketio import SocketIO

app = Flask(__name__, static_url_path='/assets', static_folder='../build/assets')
# app.config.from_object('config')
app.config['SECRET_KEY'] = 'I pee in the shower'

io = SocketIO(app)
