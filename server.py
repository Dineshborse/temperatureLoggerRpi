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
def temperatureRPi1(sid,temp):
    print('temperatureRPi1 =', sid,temp)

@sio.on('temperatureRPi2')
def temperatureRPi2(sid,temp):
    print('temperatureRPi3 =', sid,temp)

@sio.on('temperatureRPi3')
def temperatureRPi3(sid,temp):
    print('temperatureRPi3 =', sid,temp)

@sio.on('monitordata')
def monitordata(sid,data):#cpu,mem_info,disk_info,cpu_temp
    print('temperatureRPi3 =',data[3])
    print("CPU Info–> ", data[0])
    print("Memory Info–>", data[1])
    print("Disk Info–>", data[2])

@sio.on('CPU-Info3')
def CPU(sid,load):
    print('CPU Info3 =', sid,load)

@sio.on('Memory-Info3')
def Memory(sid,memusage):
    print('Memory-Info3 =', sid,memusage)

@sio.on('Disk-Info3')
def Disk(sid,diskusage):
    print('Disk-Info3 =', sid,diskusage)


def hello_world(env, start_response):
    # start_response('200 OK', [('Content-Type', 'text/plain')])
    return ['Hello, World!\r\n']

wsgi.server(eventlet.listen(('', 5555)), app)