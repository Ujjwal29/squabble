import socket
from _thread import *
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1024))
s.listen(5)
print("Listining for connections...")

def threaded_client(conn):
    mesgno = 0
    while (mesgno<5):
        newmesg = conn.recv(2048).decode("utf-8")
        print(f"message receieved: {newmesg}")
        mesgno += 1


while True:
    conn, addr = s.accept()
    print(f"Connection to {addr} established.")
    conn.send(bytes("test mesg!", "utf-8"))
    start_new_thread(threaded_client, (conn, ))

