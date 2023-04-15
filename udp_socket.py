import socket
import json
from flask_socketio import SocketIO
# Set up UDP socket: Not working still in progress
UDP_IP = "127.0.0.1"
UDP_PORT = 5001
BUFFER_SIZE = 1024
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

def listen_socket():
    udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp.bind((UDP_IP, UDP_PORT))
    print("UDP server up and listening")

    while True:
        data, addr = udp.recvfrom(bufferSize)
        message = data.decode('utf-8')
        print(f"Received message from {addr}: {message}")
        socketio.emit('update', message)

