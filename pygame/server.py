import socket
from _thread import *
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1024))
s.listen(5)
print("Listening for connections...")

def threaded_client(conn):
    while True:
        try:
            newmesg = conn.recv(2048).decode("utf-8")
            print(f"message receieved: {newmesg}")
        except:
            break
    print("Lost Connection!")
    conn.close()


while True:
    conn, addr = s.accept()
    print(f"Connection to {addr} established.")
    conn.send(bytes("You've been connected to the server.", "utf-8"))
    start_new_thread(threaded_client, (conn, ))

