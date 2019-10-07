import socketio
import time
import asyncio

sio = socketio.Client()


# This is a client script in python, it must emulate  what in a browser happends


@sio.event
def connect():
    print('(client) connection established ... ')

@sio.event
def disconnect():
    print('(client) disconnected from server ...')

@sio.event
def message(data):
    print('I received a message! (im the client): {}'.format(data))


def sendmsg(data):
    print("sendmsg from client..........{}".format(data))   
    my_data= { 'text': data }
    sio.emit('message', my_data)


if __name__ == '__main__':
    sio.connect('http://localhost:8080')
    time.sleep(2)
    sendmsg("SCRIPT de python")

