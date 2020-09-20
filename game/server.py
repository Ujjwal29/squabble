import socket
from _thread import *
import pickle
import sys
HEADERSIZE = 10
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1024))
s.listen(5)
print("Listening for connections...")

def threaded_client(conn):
    while True:
        full_msg = b''
        new_msg = True
        while True:
            msg = conn.recv(100)
            if new_msg:
                print("new msg len:", msg[:HEADERSIZE])
            #    msglen = int(msg[:HEADERSIZE])
            #    new_msg = False

            #print(f"full message length: {msglen}")

            full_msg += msg

            #print(len(full_msg))

            #if len(full_msg) - HEADERSIZE == msglen:
            #    print("full msg recvd")
            #    print(full_msg[HEADERSIZE:])
            print(pickle.loads(full_msg[HEADERSIZE:]))
            new_msg = True
            full_msg = b""

            #newmesg = conn.recv(1024).decode("utf-8")
            #newmesg = pickle.loads(newmesg)
            #print(f"message receieved: {newmesg}")
        #except:
         #   break
    conn.close()
    print("Lost Connection!")


while True:
    conn, addr = s.accept()
    print(f"Connection to {addr} established.")
    conn.send(bytes("You've been connected to the server.", "utf-8"))
    start_new_thread(threaded_client, (conn, ))

