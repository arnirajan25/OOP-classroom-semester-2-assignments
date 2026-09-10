import xmlrpc.client

server = xmlrpc.client.ServerProxy("http://127.0.0.1:8000")

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

result = server.multiply(a, b)

print("Result:", result)
