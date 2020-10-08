#!/usr/bin/env python

import sys
import socket
import time
import random 
from eurex_messages_short import Sample
from decimal import Decimal

TCP_IP = '127.0.0.1'
#TCP_IP = '192.168.178.102'
TCP_PORT = 5005
BUFFER_SIZE = 1024
MESSAGE = bytes([0x02])

#TIME_INTRO = 20
TIME_INTRO = 2
#TIME_QUEST = 30
TIME_QUEST = 3
#TIME_UNTIL_RESTART = 3
TIME_UNTIL_RESTART = 3

state_counter = 0


def main():
	global state_counter
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((TCP_IP, TCP_PORT))
	sample = Sample()
	while (1): # until CTRL+C
		if (state_counter == 0): # VR startet
			sample.flags1 = 0
			s.send(sample.serialized())
			time.sleep(1)
			state_counter = 1

		if (state_counter == 1): # Intro startet
			sample.flags1 = 1
			s.send(sample.serialized())
			time.sleep(TIME_INTRO)
			state_counter = 2

		if (state_counter == 2): # send random quest
			sample.flags1 = random.randint(6, 9)
			s.send(sample.serialized())
			time.sleep(TIME_QUEST)
			state_counter = 3

		if (state_counter == 3): # send random mission result
			sample.flags1 = random.randint(2, 3)
			s.send(sample.serialized())
			time.sleep(TIME_UNTIL_RESTART)
			state_counter = 0


if __name__ == "__main__":
	main()
