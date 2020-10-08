#!/usr/bin/env python
import socket
import random
import copy
import time

from eurex_messages_short import states, Sample


# TCP_IP = '127.0.0.1'
TCP_IP = '192.168.178.201'
TCP_PORT = 5005
BUFFER_SIZE = 64  # Normally 1024, but we want fast response


def network_server():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind((TCP_IP, TCP_PORT))
	s.listen(1)

	while 1:
		conn, addr = s.accept()
		print('Connection address: ', addr)
		sample = Sample()
		received_sample = Sample()

		while 1:
			data = conn.recv(BUFFER_SIZE)
			if not data:  # EOF
				break
			# print("received data: ", data)
			received_sample.deserialize(data)
			# print(received_sample)
			# print("State changed from '{0}' ({1}) to '{2}' ({3})".format(states[sample.flags1], sample.flags1, states[received_sample.flags1], received_sample.flags1))

			print("State changed from '{0} to '{1}'".format(sample.flags1, received_sample.flags1))

			sample = copy.copy(received_sample)
			del data

		print("Connection was closed")
		conn.close()


if __name__ == "__main__":
	network_server()
	time.sleep(2)

	print("Ende")
