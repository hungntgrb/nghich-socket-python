import socket
import sys

HOST = '192.168.1.24'
PORT = 5656
ADDR = (HOST, PORT)
ENCODING = 'utf-8'
HEADER = 20  # "16            "
DISCONNECT_MSG = '!D'

USERNAME = input('Your username? > ')  # Ko qua 20 chars.

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(ADDR)


def send(msg):
    username = USERNAME.ljust(HEADER)
    header = f"{len(msg):<{HEADER}}"

    msg = (username + header + msg).encode(ENCODING)

    sock.sendall(msg)
    print('-- Sent!')


while True:
    message = input("Your msg > ")

    send(message)

    if message == DISCONNECT_MSG:
        break

print('End session!')
