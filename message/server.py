import socket
import threading
import logging

HEADER = 64
FORMAT = 'utf-8'
PORT = 12345
SERVER = socket.gethostbyname(socket.gethostname())
print(SERVER)
ADDR = (SERVER, PORT)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# print(server)
server.bind(ADDR)
DISCONNECT_MESSAGE = "!DISCONNECT"
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def handle_client(conn, addr):
    print(f'[NEW CONNECTION] {addr} connected.')

    connected = True
    while connected:
        print(f"[ACCTUAL RECEIVE] :: {conn}, ['ADDR]:: {addr}")
        msg_length = conn.recv(HEADER).decode(FORMAT)
        
        if msg_length:
            msg_length = int(msg_length)
            print(f'[Length] :: {msg_length}')
            msg = conn.recv(msg_length).decode(FORMAT)
            print(f'[{addr}] {msg}')
            if msg == DISCONNECT_MESSAGE:
                connected = False
            # print(f"[{addr}] {msg}")
            conn.send("Msg received".encode(FORMAT))

    conn.close()

def start():
    server.listen()
    print(f'[LISTENING] Server is listening on {SERVER}')
    while True:
        conn, addr = server.accept()
        threrad = threading.Thread(target=handle_client, args=(conn, addr))
        threrad.start()
        print('[ACTIVE CONNECTIONS]', threading.active_count() - 1)


if __name__ == '__main__':
    print('[STARTING] server is starting...')
    start()       
