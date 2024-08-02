import logging
import socket
import threading
# Set a default socket timeout
socket.setdefaulttimeout(500)

HEADER = 64
FORMAT = 'utf-8'
PORT = 12345
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
print(SERVER)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)
server.listen()
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')





def handle_client(conn, addr):
    logging.info(f'[NEW CONNECTION] {addr} connected.')

    connected = True
    while connected:
        try:
            msg_bytes = conn.recv(HEADER).decode(FORMAT)
            if msg_bytes:
                print(f"[{addr}] {msg_bytes}")
                # msg = conn.recv(msg_bytes).decode(FORMAT)
                # if msg_bytes and msg.startswith("<START>"):
                #     msg_length = len(msg_bytes[2:])
                
                #     logging.info(f'[{addr}] {msg}')
    
                #     if msg == "!DISCONNECT":
                #         connected = False
                # else:
                #     logging.warning(f'[{addr}] Received unexpected data, ignoring.')
                    
                conn.sendall("Msg received".encode(FORMAT))
                
        except ConnectionResetError:
            logging.warning(f'[{addr}] Connection reset by peer.')
            break

    conn.close()

def start():
    try:
        
        logging.info(f'[LISTENING] Server is listening on {SERVER}')

        while True:
            conn, addr = server.accept()
            threading.Thread(target=handle_client, args=(conn, addr)).start()
            logging.info('[ACTIVE CONNECTIONS] %s', threading.active_count() - 1)

    except Exception as e:
        logging.error(f'Error starting server: {e}')

    finally:
        server.close()

if __name__ == "__main__":
    start()