import socket

HOST = "127.0.0.1"
PORT = 2000

inSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
inSocket.connect((HOST, PORT))
name = input('Escriba su nombre: ')
nameToBytes = bytes(name, encoding='utf-8')
inSocket.sendall(nameToBytes)
data = inSocket.recv(4096)

print(f"Received {data!r}")