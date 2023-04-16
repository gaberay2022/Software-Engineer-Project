import socket
import threading
import queue

messages = queue.Queue()
traffic = []

server=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(("127.0.0.1", 7500))


def recieve():
    while True:
        try:
            message = server.recvfrom(1024)
            action = message.decode()
            print(action)
        except:
            pass