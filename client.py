import socket
import threading
from connection import HOST, PORT, encode, decode

username = input("Escriba su nombre: ")

# conexion al servidor
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

# fn que escucha mensajes del servidor y muestra los necesarios en consola
def receive_from_server():
    while True:
        try:
            message = decode(client.recv(1024))
             # si el servidor envia USERNAME, se envia el nombre que el usuario escribio
            if message == 'USERNAME':
                client.send(encode(username))
            else:
                print(message)
        except:
            client.close()
            break

# fn para mandar mensajes al servidor
def write():
    while True:
        msg = input('')
        message = '{}--> {}'.format(username, msg)
        client.send(encode(message))
        # si el mensaje es 'chao' se envia el mensaje al servidor y se cierra la conexion
        if msg == 'chao':
            client.close()
            break

# inicio de threads para escuchar y escribir al servidor
receive_thread = threading.Thread(target=receive_from_server)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()