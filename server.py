import socket
import sys

HOST = 'localhost'
PORT = 5656
ADDR = (HOST, PORT)
NUM_OF_CLIENTS = 2

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

server.listen(NUM_OF_CLIENTS)

while True:
    print('[SERVER] is running...')
    conn, client_addr = server.accept()

    try:
        while True:
            data = conn.recv(8)
            print(f'Received {data!r} from {client_addr!r}')

            if data:
                print(f'Echo back data...')
                conn.sendall(data)
            else:
                print(f'No data from {client_addr}')
                break
    finally:
        print('[SERVER] is closing!')
        print("========================================")
        conn.close()
