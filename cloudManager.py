import socket               # Import socket module
from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket # pip install git+https://github.com/dpallot/simple-websocket-server.git
import base64
import time
import threading

# Load an color image in grayscale


wsstreamport = 1114
wscmdport=1111
UDP_IP = "172.16.62.1"
UDP_PORT = 25500
MAX_SIZE=65000
WS = None
data=''
sockToDrone = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) 

class Simplestream(WebSocket):

    def handleMessage(self):
        self.sendMessage(u''+data)
        # print('sent ws', data[:15])

    def handleConnected(self):
        print(self.address, 'connected')
         
        

    def handleError(self, error):
        print (error)
    
    def handleClose(self):

        print(self.address, 'closed')


class Simplecmd(WebSocket):

    def handleMessage(self):
        print(self.data)
        try:
            sockToDrone.sendto(self.data,("172.16.62.129", 1109))
        except socket.error as e:
            print(e)
    def handleConnected(self):
        print(self.address, 'connected')
         
        

    def handleError(self, error):
        print (error)
    
    def handleClose(self):

        print(self.address, 'closed')

class WSThread ():
    def __init__(self,port, type , data_rate=1.0):
        self.type = type
        self.port = port
        self.data_rate = data_rate
        t = threading.Thread(target=self.run)
        t.setName('no name')
        t.start()
    
    def run ( self ):
        server = SimpleWebSocketServer('', self.port, self.type)
        server.serveforever()







wss= WSThread(wsstreamport, Simplestream  )
wsc= WSThread(wscmdport, Simplecmd)
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT)) 
while True:
    data, addr = sock.recvfrom(MAX_SIZE)
    #print(addr)

