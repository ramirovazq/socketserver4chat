from aiohttp import web
import socketio
import aiohttp_cors

sio = socketio.AsyncServer(async_mode='aiohttp', cors_allowed_origins='*')
app = web.Application()
# enabling cors for demo
cors = aiohttp_cors.setup(app, defaults={
    "*": aiohttp_cors.ResourceOptions(
            allow_credentials=True,
            expose_headers="*",
            allow_headers="*",
        )
    }) # returns `aiohttp_cors.CorsConfig`

for route in list(app.router.routes()):
    if route.raw_match("/socket.io/"): # jump
        continue
    cors.add(route)
sio.attach(app)

async def index(request):
    """Serve the client-side application."""
    with open('index.html') as f:
        return web.Response(text=f.read(), content_type='text/html')

@sio.event
async def connect(sid, environ):
    msg_conectado = "usuario nuevo {} conectado".format(sid)
    print(msg_conectado)
    await sio.emit('message', "Usuario nuevo conectado.")

@sio.event
async def disconnect(sid):
    msg_desconectado = "usuario {} desconectado".format(sid)
    print(msg_desconectado)
    await sio.emit('message', "Usuario desconectado.")

@sio.on('message')
async def print_message(sid, message):
    print("____________inicio__________")
    print(message)
    try:
        if 'text' in message.keys():
            el_text = message['text']
            await sio.emit('message', el_text)
    except AttributeError:
        await sio.emit('message', message)
    print("____________fin_____________")


app.router.add_static('/static', 'static')
app.router.add_get('/', index)

if __name__ == '__main__':
    web.run_app(app)
