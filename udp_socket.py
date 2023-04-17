import socket
import queue
import json

def recieve():

    server=socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    server.bind(("127.0.0.1", 7500))

    message, addr = server.recvfrom(1024)

    clientMsg = "Message from Client: {}".format(message)
    clientIP  = "Client IP Address: {}".format(addr)

    print(clientMsg)
    print(clientIP)

    server.sendto(str.encode("Hello"), addr)

    return message.decode("utf-8")