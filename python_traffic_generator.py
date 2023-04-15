import socket
import random
import time

#should work just working on receiving packages
bufferSize = 1024
serverAddressPort = ("127.0.0.1", 5001)


def generate_traffic(red1, red2, green1, green2, counter):
	
    # Get the request data
	data = request.json
	red1 = data['red1']
	red2 = data['red2']
	green1 = data['green1']
	green2 = data['green2']
	counter = data['counter']

	# Create datagram socket
	udp = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
	serverAddressPort = ("127.0.0.1", 5001)

	# counter number of events, random player and order
	i = 1
	while i < int(counter):
		if random.randint(1,2) == 1:
			redplayer = red1
		else:
			redplayer = red2

		if random.randint(1,2) == 1:
			greenplayer = green1
		else: 
			greenplayer = green2

		if random.randint(1,2) == 1:
			message = redplayer + ":" + greenplayer
		else:
			message = greenplayer + ":" + redplayer

		print(message)
		i += 1
		udp.sendto(str.encode(str(message)), serverAddressPort)
		time.sleep(random.randint(1,3))

