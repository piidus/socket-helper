import socket

HEADER = 64
PORT = 12345  # Ensure this matches the server port
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = '192.168.0.101'  # Use localhost for testing on the same machine
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    client.connect(ADDR)
except ConnectionRefusedError as e:
    print("Connection Refused. Is the server running?", e)


def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))

if __name__ == "__main__":
    send("Hello World")
    send(input('Enter message: '))
    send("Hello World")
    send(input('Enter message: '))
    send(DISCONNECT_MESSAGE)
