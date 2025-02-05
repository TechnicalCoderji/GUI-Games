import socket
import pickle

#class responsable for connecting server
class Network:

    def __init__(self, server):
        self.client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.server = server
        self.port = 5555
        self.addr = (self.server,self.port)
        self.p = self.connect()
    
    def get_p(self):
        return self.p 

    def connect(self):
        try:
            self.client.connect(self.addr)
            return self.client.recv(1024).decode()
        except:
            pass
    
    def send(self, data):
        try:
            self.client.send(str.encode(data))
            return pickle.loads(self.client.recv(1024))
        except socket.error as e:
            print(e)

# if current file runing
if __name__ == "__main__":
    pass