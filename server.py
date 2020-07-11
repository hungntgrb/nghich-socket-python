import socket
import sys
import threading

from utils import isClosed, ENCODING, DISCONNECT_MSG, HEADER, ABORTED_MSG, ACCEPTED_MSG

HOST = socket.gethostbyname(socket.gethostname())
PORT = 5656
ADDR = (HOST, PORT)

BLACK_LIST = ['192.168.1.26']


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)


def receive(conn):
    if not isClosed(conn):
        # print('receive runs!')
        username = conn.recv(HEADER).decode(ENCODING).strip()
        get_length = conn.recv(HEADER).decode(ENCODING)
        # if msg_length:
        msg_length = int(get_length)
        msg = conn.recv(msg_length).decode(ENCODING)  # Het msg.
        # print('End Receive func.')
        return (username, msg)
    return ('No user', 'No msg')


def handle_client(conn, addr):
    """Receive msg from Client & output to console."""
    print(f"\n[NEW CONNECTION] {addr} CONNECTED!")

    while True:
        username, msg = receive(conn)
        if msg == DISCONNECT_MSG:
            break
        print(f"[ {username} ] {msg}")

    print(f"-- {username} -- has exited!")
    conn.close()


def start():
    print(f"[SERVER] Server is listening on :{PORT}")
    print('-----------------------------------------')
    server.listen()

    while True:
        conn, client_addr = server.accept()  # Cho connect tu Client.

        if client_addr[0] in BLACK_LIST:
            conn.send(ABORTED_MSG.encode(ENCODING))
            conn.close()
        else:
            conn.send(ACCEPTED_MSG.encode(ENCODING))
        # Tao 1 thread cho moi client.
        if not isClosed(conn):
            thread = threading.Thread(
                target=handle_client, args=(conn, client_addr))
            thread.start()

        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}\n")


if __name__ == '__main__':
    print(f"\n[SERVER] Server is starting...")
    start()
