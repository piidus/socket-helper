import socket
import threading
from global_variable import HEADER, FORMAT, DISCONNECT_MESSAGE

PORT = 12345  # Ensure this matches the server port
SERVER = '192.168.0.101'  # Use localhost for testing on the same machine
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    client.connect(ADDR)
except ConnectionRefusedError as e:
    print("Connection Refused. Is the server running?", e)

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if  message == DISCONNECT_MESSAGE:
                break
            print(f"\nReceived: {message}")
        except ConnectionResetError:
            break
def main():
    receive_thread = threading.Thread(target=receive_messages, args=(client,))
    receive_thread.start()
    
    while True:
        message = input("Enter message: ")
        client.send(message.encode('utf-8'))

if __name__ == "__main__":
    main()