import socket
import sys
import threading

from utils import isClosed, ENCODING, DISCONNECT_MSG, HEADER, ABORTED_MSG, ACCEPTED_MSG

HOST = socket.gethostbyname(socket.gethostname())
PORT = 5656
ADDR = (HOST, PORT)

BLACK_LIST = ['192.168.1.26']
ACTIVE_CLIENTS = []


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)


def addr_to_str(addr):
    x = ':'.join(map(str, addr))
    return x


def receive(conn):
    if not isClosed(conn):
        # print('receive runs!')
        try:
            username = conn.recv(HEADER).decode(ENCODING).strip()
            get_length = conn.recv(HEADER).decode(ENCODING)
            msg_length = int(get_length)
            msg = conn.recv(msg_length).decode(ENCODING)  # Het msg.
            return (username, msg)

        except ConnectionResetError:
            conn.close()
            print("[CLIENT-SIDE] Connection lost unexpectedly!")
            return conn


def handle_client(conn, addr):
    """Receive msg from Client & output to console."""
    print(f"\n[NEW CONNECTION] {addr} CONNECTED!")

    while True:
        if isClosed(conn):
            break
        try:
            username, msg = receive(conn)
        except (ValueError, TypeError):
            break
        if msg == DISCONNECT_MSG:
            break
        print(f"[ {username} ] {msg}")

    ACTIVE_CLIENTS.pop()
    try:
        print(f"-- {username} -- has exited!")
    except UnboundLocalError:
        print('-- [Client] -- has exited! Unknown username due to no first message.')

    conn.close()
    return (conn, addr)


def start():
    server.listen()

    while True:
        conn, client_addr = server.accept()  # Cho connect tu Client.

        if client_addr[0] in BLACK_LIST:
            conn.send(ABORTED_MSG.encode(ENCODING))
            conn.close()
        else:
            ACTIVE_CLIENTS.append(conn)
            conn.send(ACCEPTED_MSG.encode(ENCODING))
        # Tao 1 thread cho moi client.
        if not isClosed(conn):
            thread = threading.Thread(
                target=handle_client, args=(conn, client_addr))
            thread.start()
        else:
            ACTIVE_CLIENTS.pop()

        print(f"\n[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")
        print(f'[CONN LIST] {len(ACTIVE_CLIENTS)}')
        print('-----------------------------------------')


if __name__ == '__main__':
    print(f"\n[SERVER] Server is listening on {HOST}:{PORT}")
    print('-----------------------------------------')
    start()
