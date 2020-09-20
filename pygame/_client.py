import socket
import pickle
class client:
    def __init__(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((socket.gethostname(), 1024))

    def send_mesg(self, mesg):
        self.mesg = mesg
        self.s.send(bytes(self.mesg, "utf-8"))
    def send_list(self, mesg):
        a = 10
        self.mesg = mesg
        self.mesg = pickle.dumps(self.mesg)
        self.mesg = bytes(f'{len(self.mesg):<{a}}', "utf-8") + self.mesg
        print(self.mesg)
        self.s.send(self.mesg)
        #print(self.mesg)
#c2 = client()
#c2.send_list({1:"hello"})