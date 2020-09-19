import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1024))
complete_info = ""
while True:
    msg = s.recv(2048)
    if len(msg) <= 0:
        break
    mesg_received =  msg.decode("utf-8")
    print(mesg_received)
    mesgno = 0
    while (mesgno<5):
        newmesg = input("mesg? : ")
        s.send(bytes(newmesg, "utf-8"))
        mesgno += 1

