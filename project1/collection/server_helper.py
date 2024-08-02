from .global_variable import HEADER, FORMAT, DISCONNECT_MESSAGE, clients


def broadcast(message, sender_socket):
    for client in clients:
        if client != sender_socket:
            try:
                client.send(message.encode('utf-8'))
            except Exception as e:
                print(f"Error sending message: {e}")

def handle_client(client_socket, client_address):
    print(f"Accepted connection from {client_address}")
    clients.append(client_socket)
    
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            print(f"Received from {client_address}: {message}")
            broadcast(message, client_socket)
        except ConnectionResetError:
            break
    
    print(f"Connection closed by {client_address}")
    clients.remove(client_socket)
    client_socket.close()


