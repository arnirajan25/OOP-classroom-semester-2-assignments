import socket

HOST = "127.0.0.1"
PORT = 5000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind((HOST, PORT))
server_socket.listen(1)

print("Server is waiting for a connection...")

connection, address = server_socket.accept()

print("Connected by:", address)

message = connection.recv(1024).decode()

print("Client sent:", message)

connection.send("Message received!".encode())

connection.close()
server_socket.close()
