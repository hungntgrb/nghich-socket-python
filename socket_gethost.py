import socket

name = socket.gethostname()
print(name)
print(socket.gethostbyname(name))
