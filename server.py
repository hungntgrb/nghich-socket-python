import socket
import sys
import threading

HOST = socket.gethostbyname(socket.gethostname())
PORT = 5656
ADDR = (HOST, PORT)
HEADER = 20
ENCODING = 'utf-8'
DISCONNECT_MSG = '!D'


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)


def receive(conn):
    if conn:
        # print('receive runs!')
        username = conn.recv(HEADER).decode(ENCODING).strip()
        get_length = conn.recv(HEADER).decode(ENCODING)
        # if msg_length:
        msg_length = int(get_length)
        msg = conn.recv(msg_length).decode(ENCODING)  # Het msg.
        # print('End Receive func.')
        return (username, msg)


def handle_client(conn, addr):
    """Receive msg from Client & output to console."""
    print(f"[NEW CONNECTION] {addr} CONNECTED!")

    while True:
        username, msg = receive(conn)

        if msg == DISCONNECT_MSG:
            break

        print(f"[ {username} ] {msg}")

    print(f"-- {username} -- has exited!")
    conn.close()


def start():
    print(f"[SERVER] Server is listening on :{PORT}")
    server.listen()

    while True:
        conn, client_addr = server.accept()  # Cho connect tu Client.
        # Tao 1 thread cho moi client.
        thread = threading.Thread(
            target=handle_client, args=(conn, client_addr))
        thread.start()

        print(f"[ACTIVES] {threading.activeCount() - 1}")


if __name__ == '__main__':
    print(f"\n[STARTING] Server is starting...")
    start()
