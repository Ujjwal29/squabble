import socket

class client:
    def __init__(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((socket.gethostname(), 1024))

    def send_mesg(self, mesg="asd"):
        self.mesg = mesg
        self.s.send(bytes(mesg, "utf-8"))

