import socket
import sys

from utils import isClosed, ENCODING, DISCONNECT_MSG, HEADER, ABORTED_MSG, ACCEPTED_MSG

HOST = '192.168.1.24'  # Connect to...
PORT = 5656
ADDR = (HOST, PORT)


USERNAME = input('Your username > ')  # Ko qua 20 chars.

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(ADDR)

ini_msg = sock.recv(100).decode(ENCODING)

if ini_msg.startswith(ABORTED_MSG):
    sock.close()
elif ini_msg.startswith(ACCEPTED_MSG):
    print('[SERVER] Server is listening to you...')


def build(msg):
    username = USERNAME.ljust(HEADER)
    header = f"{len(msg):<{HEADER}}"
    return (username + header + msg).encode(ENCODING)


# Loop ask for msg & send it
while True:

    if not isClosed(sock):
        message = input("Your msg > ")
    else:
        break

    built_message = build(message)

    try:
        sock.send(built_message)
    except ConnectionAbortedError:
        print('[ABORTED!] The server aborted your connection.')
        break

    if message == DISCONNECT_MSG:
        break

print(' End session! '.center(50, '-'))
