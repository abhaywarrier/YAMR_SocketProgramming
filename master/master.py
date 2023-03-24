import socket
import os

# device's IP address
SERVER_HOST = socket.gethostbyname(socket.gethostname())
SERVER_PORT = 5050
# receive 4096 bytes each time
BUFFER_SIZE = 4096
SEPARATOR = "<SEPARATOR>"

# create the server socket
# TCP socket
s = socket.socket()

# bind the socket to our local address
s.bind((SERVER_HOST, SERVER_PORT))

# enabling our server to accept connections
# 5 here is the number of unaccepted connections that
# the system will allow before refusing new connections
s.listen(5)
print(f"[*] Master Listening as {SERVER_HOST}:{SERVER_PORT}")

# accept connection if there is any
client_socket, address = s.accept() 
# if below code is executed, that means the sender is connected
print(f"[+] {address} is connected.")
# receive the file infos
# receive using client socket, not server socket

received = client_socket.recv(BUFFER_SIZE).decode()
filename, filesize  = received.split(SEPARATOR)
print(filename)

metadata = open("metadata.txt","w")
fname = os.stat(filename)
fname = str(fname)
metadata.write(fname)
metadata.close()


receive = client_socket.recv(1024).decode()

