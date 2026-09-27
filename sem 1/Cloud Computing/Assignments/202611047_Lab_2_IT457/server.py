import socket
import threading
HOST = "127.0.0.1"
PORT = 5050
def handle_client(client_socket, client_address):
    print(f"Client connected: {client_address}")
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        message = data.decode()
        print(f"Message from {client_address}: {message}")
        response = f"Server received: {message}"
        client_socket.send(response.encode())
    print(f"Client disconnected: {client_address}")
    client_socket.close()
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()
print(f"Server is running on {HOST}:{PORT}")
while True:
    client_socket, client_address = server_socket.accept()
    client_thread = threading.Thread(
        target=handle_client,
        args=(client_socket, client_address)
    )
    client_thread.start()