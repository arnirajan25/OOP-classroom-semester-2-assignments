import socket

HOST = "127.0.0.1"
PORT = 5000

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect((HOST, PORT))

message = "Hello from Nirajan!"

client_socket.send(message.encode())

response = client_socket.recv(1024).decode()

print("Server replied:", response)

client_socket.close()
