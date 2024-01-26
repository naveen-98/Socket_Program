import socket
import time
import os
import platform
import threading

class Client:

    def __init__(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_ip = self.get_server_ip()
        self.server_port = 12345

    def get_server_ip(self):
        while True:
            server_ip = input('Enter server IP: ')
            if len(server_ip.split('.')) == 4:
                return server_ip
            else:
                print('Invalid IP address format. Please try again.')

    def make_connection(self):
        ''' Sending connection request to the server node '''
        while True:
            try:
                server = (self.server_ip, self.server_port)
                self.client_socket.connect(server)
                print('Connection successful to the server')
                return True
            except Exception as e:
                print(f'Error: {e}')
                time.sleep(1)

    def send_sms(self, msg):
        ''' Sending the message to the connected Server '''
        self.client_socket.send(msg.encode())

    def receive_sms(self):
        ''' Receiving message from the node server'''
        while True:
            data = self.client_socket.recv(1024).decode()
            if not data:
                break
            print(data)

    def chat_room(self):
        if self.make_connection():
            receiving_thread = threading.Thread(target=self.receive_sms)
            receiving_thread.daemon = True
            receiving_thread.start()

            while True:
                message = input('Your message: ')
                if message.lower() == 'exit':
                    break
                formatted_message = f"\nClient: {message}\n"
                self.send_sms(formatted_message)

if __name__ == '__main__':
    client_instance = Client()
    client_instance.chat_room()
