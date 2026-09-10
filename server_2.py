import socket

HOST = "127.0.0.1"
PORT = 5001

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind((HOST, PORT))
server_socket.listen(1)

print("Server is waiting for a client...")

connection, address = server_socket.accept()

print("Client connected:", address)

connection.send("What is your name? ".encode())

name = connection.recv(1024).decode()

print("Client's name:", name)

greeting = f"Hello, {name}! Welcome to the server."

connection.send(greeting.encode())

connection.close()
server_socket.close()
