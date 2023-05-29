import socket
import threading
from connection import HOST, PORT, encode, decode

# inicia servidor
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()
print('Servidor iniciado y contestando OK')

clients = [] # guarda la informacion de address de los clientes
usernames = [] # guarda los nombres seleccionados por los clientes

# fn para enviar un mensaje a todos los clientes
def broadcast_message(message):
    for client in clients:
        client.send(message)

# fn que maneja los mensajes que envian los clientes
def handle_incoming_messages(client):
    while True:
        try:
            message = client.recv(1024) # recepcion del mensaje
            broadcast_message(message) # envio a todos los clientes
            if message == 'chao':
                break
        except:
            # si el usuario escribe 'chao' o hay un error, se elimina el cliente y se notifica de la salida
            index = clients.index(client)
            clients.remove(client)
            client.close()
            username = usernames[index]
            exit_alert = 'El usuario "{}" abandono'.format(username)
            print(exit_alert)
            broadcast_message(encode(exit_alert))
            usernames.remove(username)
            break

# fn para escuchar mensajes de los clientes
def receive_messages():
    while True:
        # aceptar la conexion y obtener la informacion necesaria del cliente
        client, address = server.accept()

        # anadir el username a la lista y mandarlo a todos los clientes
        client.send(encode('USERNAME'))
        username = decode(client.recv(1024))
        usernames.append(username)
        clients.append(client)
        new_user_alert = 'Usuario "{}" conectado'.format(username)
        print(new_user_alert)
        broadcast_message(encode(new_user_alert))

        # inicio del thread para manejar al cliente
        thread = threading.Thread(target=handle_incoming_messages, args=(client,))
        thread.start()

receive_messages()