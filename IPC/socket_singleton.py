from sys import argv
from socket import socket
from threading import Thread


class Socket_Singleton():
    def __init__(self, client=True, port=1337):
        self.arguments = [arg for arg in argv[1:]]
        self.port = port
        self.client = client
        self.sock = socket()
        self.socket_handler()
        
    
    def socket_handler(self):
        try:
            self.sock.bind(("127.0.0.1", self.port))
        except:
            if self.client:
                self.create_client()
                raise SystemExit
            else:
                raise SystemExit
        else:
            thread = Thread(target=self.create_server, daemon=True)
            thread.start()


    def create_server(self):
        with self.sock as s:
            s.listen()
            while True:
                connection, address = s.accept()
                with connection:
                    data = connection.recv(1024)
                    if data:
                        args = data.decode().split()
                        [self.arguments.append(arg) for arg in args]


    def create_client(self):
        with self.sock as s:
            s.connect(("127.0.0.1", self.port))
            for arg in argv[1:]:
                s.send(arg.encode())
                s.send(" ".encode())
