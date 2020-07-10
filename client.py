import socket
import sys

HOST = 'localhost'
PORT = 5656
ADDR = (HOST, PORT)
ENCODING = 'utf-8'

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(f'Connecting to {HOST!r} port {PORT!r}')
sock.connect(ADDR)


try:
    msg = input("Your name > ").encode(ENCODING)
    sock.sendall(msg)

    amount_received = 0
    amount_expected = len(msg)
    while amount_received < amount_expected:
        data = sock.recv(8)
        amount_received += len(data)
        print(f'Received {data!r}')

finally:
    print('Closing connection!')
    sock.close()
