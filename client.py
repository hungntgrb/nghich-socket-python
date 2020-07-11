import socket
import sys

HOST = '192.168.1.24'
PORT = 5656
ADDR = (HOST, PORT)
ENCODING = 'utf-8'
HEADER = 20
DISCONNECT_MSG = '!DISCONNECT'

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect(ADDR)


def send(msg):
    header = f"{len(msg):<{HEADER}}"
    msg = (header + msg).encode(ENCODING)
    sock.sendall(msg)
    print('-- Sent!')


while True:
    message = input("Your msg > ")

    send(message)

    if message == DISCONNECT_MSG:
        sock.close()
        break

print('End Client!')
