#!/usr/bin/python3
# -*- coding: utf-8 -*-


class Message:
	pos_x = 0
	pos_y = 0
	pos_z1 = 0
	pos_z2 = 0
	pos_r = 0
	status = 0

	def deserialize(self, data):
		pos_x, pos_y, pos_z1, pos_z2, pos_r, status = data.rstrip("\r\n").split(";")
		self.pos_x = int(pos_x)
		self.pos_y = int(pos_y)
		self.pos_z1 = int(pos_z1)
		self.pos_z2 = int(pos_z2)
		self.pos_r = int(pos_r)
		self.status = int(status)

	def printout(self):
		print("X: {0:5d} ; Y: {1:5d} ; Z1: {2:4d} ; Z2: {3:4d} ; R: {4:3d} ; Status: {5:3d}".format(self.pos_x,
																									self.pos_y,
																									self.pos_z1,
																									self.pos_z2,
																									self.pos_r,
																									self.status))
