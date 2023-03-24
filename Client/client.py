import socket
import os
import tqdm

HEADER = 64
port = 5050
FORMAT = 'utf-8'
DISCONNECT_MESG = "!Disconnect"
host = socket.gethostbyname(socket.gethostname())
ADDR = (host,port)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)

    print(client.recv(2048).decode(FORMAT))

# print("Please Enter The path of file you want to write: ")
# msg = input()
SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 4096 # send 4096 bytes each time step

filename = "test.txt"
# get the file size
filesize = os.path.getsize(filename)

