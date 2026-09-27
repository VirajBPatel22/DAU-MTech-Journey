import socket
import time
HOST = "127.0.0.1"
PORT = 5050
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))
print("Connected to server.")
counter = 1
while True:
    message = f"Hello Server - Message {counter}"
    client_socket.send(message.encode())
    data = client_socket.recv(1024)
    response = data.decode()
    print("Server:", response)
    counter += 1
    time.sleep(3)