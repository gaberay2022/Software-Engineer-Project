import socket
import random
import time

#should work just working on receiving packages
traffic = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
traffic.bind("127.0.0.1", 7501)


def generate_traffic(red1, red2, green1, green2, counter):

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
		traffic.sendto(f"{message}".encode(), ("127.0.0.1", 7501))
		time.sleep(random.randint(1,3)) 

