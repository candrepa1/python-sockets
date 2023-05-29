HOST = '127.0.0.1'
PORT = 2000

# fn para pasar de string a byte
def encode(msg):
    return msg.encode('ascii')

# funcion para pasar de byte a string
def decode(msg):
    return msg.decode('ascii')
