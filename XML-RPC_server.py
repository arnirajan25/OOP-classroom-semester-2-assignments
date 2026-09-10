from xmlrpc.server import SimpleXMLRPCServer

def multiply(a, b):
    return a * b

server = SimpleXMLRPCServer(("127.0.0.1", 8000))

print("XML-RPC server is running on port 8000...")

server.register_function(multiply, "multiply")

server.serve_forever()
