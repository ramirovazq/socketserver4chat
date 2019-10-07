# socketserver4chat

Servidor de Socket, basado en aiohttp y sockeio (python3). Usado para emular servicio de chat.

### Prerequisitos

Es necesario tener:

```
virtualenv
python3
```

### Instalación

Genera un nuevo ambiente virtual y actívalo.

```
usuario@tu-maquina:~/virtualenvs$ virtualenv -p python3 chat-server-env
usuario@tu-maquina:~/virtualenvs$ $ source chat-server-env/bin/activate
```

Descarga el proyecto

```
(ecommerce-env) usuario@tu-maquina:~/virtualenvs$ cd
(ecommerce-env) usuario@tu-maquina:~$ git clone https://github.com/ramirovazq/socketserver4chat.git

```

Entra al proyecto e instala los requirements.txt

```
(ecommerce-env) usuario@tu-maquina:~$ cd socketserver4chat/
(ecommerce-env) usuario@tu-maquina:~$ pip3 install -r requirements.txt 

```

Arranca el proyecto

```
(ecommerce-env) usuario@tu-maquina:~$ python3 server.py

```

Arranca el proyecto



## Script cliente 

Se tiene un script de cliente, para probar el funcioanmeinto.

```
(ecommerce-env) usuario@tu-maquina:~$ python3 client.py
```
El servicio de socket, debe estar corriendo en 0.0.0.0:8080



## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

