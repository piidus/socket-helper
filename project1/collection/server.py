import socket
import threading

from .global_variable import clients, log
from .server_helper import handle_client, broadcast

PORT = 12345
SERVER = socket.gethostbyname(socket.gethostname())
# print(SERVER)
ADDR = (SERVER, PORT)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# print(server)
server.bind(ADDR)
# DISCONNECT_MESSAGE = "!DISCONNECT"




def start():
    server.listen()
    # print(f'[LISTENING] Server is listening on {SERVER}')
    log.info(f'[LISTENING] Server is listening on {SERVER}')
    while True:
        conn, addr = server.accept()
        threrad = threading.Thread(target=handle_client, args=(conn, addr))
        threrad.start()
        # print('[ACTIVE CONNECTIONS]', threading.active_count() - 1)
        log.info(f"[ACTIVE CONNECTIONS]', {threading.active_count() - 1}")


if __name__ == '__main__':
    print('[STARTING] server is starting...')
    start()       
