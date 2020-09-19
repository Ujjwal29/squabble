import socket
from _thread import *
import sys
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((socket.gethostname(), 1024))
except socket.error as e:
    str(e)
s.listen(2)
print("waiting for connection!")


def threaded_client(conn):
    conn.send(str.encode("Connected", "utf-8"))
    print("came here!")
    reply = ""
    while True:
        try:
            data = conn.recv(2048)
            reply = data.decode("utf-8")
            if not data:
                print("Disconnected")
                break
            else:
                print("Received: ", reply)
                print("Sending: ", reply)
            conn.sendall(str.encode(reply))
        except:
            break
    print("Lost Connection!")
    conn.close()


while True:
    conn, addr = s.accept()
    print(f"Connection to {addr} established")
    start_new_thread(threaded_client, (conn, ))
