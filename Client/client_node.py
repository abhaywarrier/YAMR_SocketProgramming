import socket
import tqdm
import os
from pathlib import Path

SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 4096 # send 4096 bytes each time step

# the ip address or hostname of the server, the receiver
host = socket.gethostbyname(socket.gethostname())
# the port, let's use 5001


# the name of file we want to send, make sure it exists

def worker1(fname):
    # p = Path(fname).resolve()
    # p = str(p)
    filename = fname
    # get the file size
    filesize = os.path.getsize(filename)

    port = 5001

    # create the client socket
    s = socket.socket()

    print(f"[+] Connecting to {host}:{port}")
    s.connect((host, port))
    print("[+] Connected.")

    # send the filename and filesize
    s.send(f"{filename}{SEPARATOR}{filesize}".encode())

    save_path = 'C:/Users/abhay/Desktop/PES/'
    save_path = str(save_path)
    name_of_file = os.path.join(save_path,filename)

    # start sending the file
    progress = tqdm.tqdm(range(filesize), f"Sending {filename}", unit="B", unit_scale=True, unit_divisor=1024)
    with open(name_of_file, "wb") as f:
        while True:
            # read the bytes from the file
            bytes_read = f.read(BUFFER_SIZE)
            if not bytes_read:
                # file transmitting is done
                break
            # we use sendall to assure transimission in 
            # busy networks
            s.sendall(bytes_read)
            # update the progress bar
            progress.update(len(bytes_read))
    return

def worker2(fname):
    p = Path(fname).resolve()
    p = str(p)
    filename = p
    # get the file size
    filesize = os.path.getsize(filename)

    port = 5002
    # create the client socket
    s = socket.socket()

    print(f"[+] Connecting to {host}:{port}")
    s.connect((host, port))
    print("[+] Connected.")

    # send the filename and filesize
    s.send(f"{filename}{SEPARATOR}{filesize}".encode())

    # start sending the file
    progress = tqdm.tqdm(range(filesize), f"Sending {filename}", unit="B", unit_scale=True, unit_divisor=1024)
    with open(filename, "rb") as f:
        while True:
            # read the bytes from the file
            bytes_read = f.read(BUFFER_SIZE)
            if not bytes_read:
                # file transmitting is done
                break
            # we use sendall to assure transimission in 
            # busy networks
            s.sendall(bytes_read)
            # update the progress bar
            progress.update(len(bytes_read))
    return

def worker3(fname):
    p = Path(fname).resolve()
    p = str(p)
    filename = p
    # get the file size
    filesize = os.path.getsize(filename)

    port = 5003
    # create the client socket
    s = socket.socket()

    print(f"[+] Connecting to {host}:{port}")
    s.connect((host, port))
    print("[+] Connected.")

    # send the filename and filesize
    s.send(f"{filename}{SEPARATOR}{filesize}".encode())

    # start sending the file
    progress = tqdm.tqdm(range(filesize), f"Sending {filename}", unit="B", unit_scale=True, unit_divisor=1024)
    with open(filename, "rb") as f:
        while True:
            # read the bytes from the file
            bytes_read = f.read(BUFFER_SIZE)
            if not bytes_read:
                # file transmitting is done
                break
            # we use sendall to assure transimission in 
            # busy networks
            s.sendall(bytes_read)
            # update the progress bar
            progress.update(len(bytes_read))
    return

def master(fname):
    p = Path(fname).resolve()
    p = str(p)
    filename = p
    # get the file size
    filesize = os.path.getsize(filename)

    port = 5050
    # create the client socket
    s = socket.socket()

    print(f"[+] Connecting to {host}:{port}")
    s.connect((host, port))
    print("[+] Connected.")

    # send the filename and filesize
    s.send(f"{filename}{SEPARATOR}{filesize}".encode())

    progress = tqdm.tqdm(range(filesize), f"Sending {filename}", unit="B", unit_scale=True, unit_divisor=1024)
    with open(filename, "rb") as f:
        while True:
            # read the bytes from the file
            bytes_read = f.read(BUFFER_SIZE)
            if not bytes_read:
                # file transmitting is done
                break
            # we use sendall to assure transimission in 
            # busy networks
            s.sendall(bytes_read)
            # update the progress bar
            progress.update(len(bytes_read))

    return

def write():
    print("Enter File Name: ")
    fname = input()
    master(fname)
    p = Path(fname).resolve()
    p = str(p)
    fname = p
    # opening the main file
    with open(fname, 'r') as file:
        data = file.readlines()
    
    # writing half of the data in one file
    with open("first_half.txt", 'w') as file1:
        for line in data[:int(len(data)/2)]:
            file1.write(line)
    
    # writing another half of the data in one file
    with open("second_half.txt", 'w') as file2:
        for line in data[int(len(data)/2):]:
            file2.write(line)

    p = Path("first_half.txt").resolve()
    first_half = str(p)
    worker1(first_half)
    p = Path("second_half.txt").resolve()
    second_half = str(p)
    worker2(second_half)



def read():
    fname = input()
    worker1(fname)

write() 