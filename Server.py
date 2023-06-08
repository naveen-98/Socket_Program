import socket
import threading
import time


class Server:

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = "127.0.0.1"
    port = 12345

    def __init__(self):
        server_config = (self.host, self.port)

        self.server.listen(5)
        self.server.bind(server_config)

        self.clientsocket, self.addr = self.server.accept()
        print("Get connecting from ", self.addr)


    def receive_sms(self):
        ''' Receiving connection from the client'''
        try:
            while True:
                data = self.clientsocket.recv(1024).decode()
                time.sleep(0.001)
                print(data)
        except Exception as ex:
            print("The below error have occured please checkout")
            print(ex)

    def chat(self):
        self.Receiving_ciao = threading.Thread(target=self.receive_sms)
        self.Receiving_ciao.daemon = True
        self.Receiving_ciao.start()
        while True:
            server_message = input()
            server_message = "\nserver:{}\n".format(server_message)
            self.clientsocket.send(server_message.encode())


if __name__ == '__main__':
    Server_m = Server()
    Server_m.chat()
    Server_m.Receiving_ciao.join()
    Server_m.server.close()
