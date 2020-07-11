import socket
import sys
import threading

HOST = socket.gethostbyname(socket.gethostname())
PORT = 5656
ADDR = (HOST, PORT)
HEADER = 20
ENCODING = 'utf-8'
DISCONNECT_MSG = '!DISCONNECT'


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)


def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} CONNECTED!")
    connected = True

    while connected:
        msg_length = conn.recv(HEADER).decode(ENCODING)
        # if msg_length:
        msg_length = int(msg_length)
        msg = conn.recv(msg_length).decode(ENCODING)

        connected = False

    print(f"[{addr}] {msg}")

    if msg == DISCONNECT_MSG:
        print(f"[{addr}] disconnected!")
        conn.close()


def start():
    print(f"[SERVER] Server is listening on {PORT}")
    server.listen()

    while True:
        conn, client_addr = server.accept()
        thread = threading.Thread(
            target=handle_client, args=(conn, client_addr))
        thread.start()
        print(f"[ACTIVES] {threading.activeCount() - 1}")


print(f"[STARTING] Server is starting...")
start()
