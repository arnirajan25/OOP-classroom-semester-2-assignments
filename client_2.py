import socket

HOST = "127.0.0.1"
PORT = 5001

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect((HOST, PORT))

question = client_socket.recv(1024).decode()

print("Server:", question)

name = input("Enter your name: ")

client_socket.send(name.encode())

greeting = client_socket.recv(1024).decode()

print("Server:", greeting)

client_socket.close()
