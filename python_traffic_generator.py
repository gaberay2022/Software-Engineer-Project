import socket
import random
import time

counter = 400

with open('./files/redTeam.txt') as f:
	red_team = f.readlines()[0].split(',')
with open ('./files/greenTeam.txt') as f:
	green_team = f.readlines()[0].split(',')

traffic = socket.socket(family = socket.AF_INET, type = socket.SOCK_DGRAM)
traffic.bind(("127.0.0.1", 7501))


i=1

# counter number of events, random player and order
while i < int(counter):
	if random.randint(1,2) == 1:
		message = "red" + ":" + str(random.randint(0,len(red_team)-1)) + ":" + str(random.randint(0,len(green_team)-1))
	else:
		message = "green" + ":" + str(random.randint(0,len(green_team)-1)) + ":" + str(random.randint(0,len(red_team)-1))

	print(message)
	i += 1
	traffic.sendto(str.encode(str(message)), ("127.0.0.1", 7500))
	time.sleep(random.randint(1,3)) 

