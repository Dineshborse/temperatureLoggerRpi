from eventlet import wsgi
import eventlet

import socketio
sio = socketio.Server(async_mode='eventlet',cors_allowed_origins='*')

sio = socketio.Server()
app = socketio.WSGIApp(sio)

@sio.on('connect')
def connect(sid, env):
    print('connect ', sid)

@sio.on('ping-from-client')
def ping_from_client(sid, env):
    print('ping-from-client ', sid,env)
    sio.emit('pong-from-server')

@sio.on('disconnect')
def disconnect(sid):
    print('disconnect ', sid)

@sio.on('temperatureRPi1')
def disconnect(sid,temp):
    print('temperatureRPi1 =', sid,temp)

@sio.on('temperatureRPi2')
def disconnect(sid,temp):
    print('temperatureRPi3 =', sid,temp)

@sio.on('temperatureRPi3')
def disconnect(sid,temp):
    print('temperatureRPi3 =', sid,temp)

def hello_world(env, start_response):
    # start_response('200 OK', [('Content-Type', 'text/plain')])
    return ['Hello, World!\r\n']

wsgi.server(eventlet.listen(('', 5555)), app)