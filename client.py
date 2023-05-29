import socketio

import time
import _thread as thread
import gpiozero as gz

sio = socketio.Client()
@sio.on('connect')
def connect():
    print('connect ')
    sio.emit("ping-from-client",["data"])
    thread.start_new_thread(my_background_task, ())

@sio.on('disconnect')
def disconnect():
    print('disconnect ')

@sio.on('pong-from-server')
def pong_from_server():
    print('pong-from-server')

def my_background_task():
    while 1:
        cpu_temp = gz.CPUTemperature().temperature
        cpu_temp = round(cpu_temp, 2)
        sio.emit('temperatureRPi3', cpu_temp)
        time.sleep(1)


sio.connect('http://13.234.208.123:5555',transports=['websocket'])


