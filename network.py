from socket import *
import pickle

#server = "192.168.1.217"
#port = 5555
#s = socket(AF_INET, SOCK_DGRAM)
class Network:
    def __init__(self):
        self.server = "192.168.1.217"
        self.port = 5555
        self.client = socket(AF_INET, SOCK_DGRAM)
        self.addr = (self.server, self.port)
        self.modifiedMessage = ""
        #self.p = self.connect()

    """def getP(self):
        return self.p"""

    """def connect(self):
        try:
            self.client.connect(self.addr)
            return pickle.loads(self.client.recv(4096))
        except:
            pass"""

    def send(self, data):
        try:
            self.client.sendto(pickle.dumps(data), self.addr)
            self.modifiedMessage, serverAddress = self.client.recvfrom(4096)
            return pickle.loads(self.modifiedMessage)
        except:
            print("error")
