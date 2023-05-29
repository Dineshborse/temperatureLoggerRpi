import socketio
sio = socketio.Client()
@sio.on('connect')
def connect():
    print('connect ')
    sio.emit("ping-from-client",["data"])

@sio.on('disconnect')
def disconnect():
    print('disconnect ')

@sio.on('pong-from-server')
def pong_from_server():
    print('pong-from-server')

sio.connect('http://192.168.0.93:5555',transports=['websocket'])


