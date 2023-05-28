import socket

HOST = "127.0.0.1" 
PORT = 2000

newSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

newSocket.bind((HOST, PORT))
newSocket.listen()
print('Servidor iniciado y contestando OK')
users = []
conn, addr = newSocket.accept()
if conn:
    print(f"Connected by {addr}")
    while True:
        data = conn.recv(4096)
        user = data.decode("utf-8") 
        users.append(user)
        print(f"Usuario '{user}' conectado")
        # if not data:
        #     break
        print(users, 'users!')
        # conn.sendall(data)