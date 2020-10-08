import struct

length = 32 # real length in bytes
STX = 0x02  # Start of Text
ETX = 0x03  # End of Text

states = {
	0: "Client reset",
	1: "Intro Video started",
	2: "Overall Mission succeeded",
	3: "Overall Mission failed",
	4: "Game paused",
	5: "Task: Dispatch Cargo",
	6: "Task: Mine Crystals",
	7: "Task: Sample Methane Sources",
	8: "Task: Measure Black Smoker",
	9: "Task: Examine Fireflies"
}

# Network Message containing all the data
class Sample:
	timestamp = 0 # timestamp in ms
	pos_x = 0     # x position
	pos_y = 0     # y position
	pos_z = 0     # z position
	pitch = 0     # horizontal rotation
	yaw = 0       # vertical rotation
	flags1 = 0    # flags 1
	flags2 = 0    # flags 2

	def serialized(self):
		r = bytearray()
		r.append(STX)

		# https://docs.python.org/3/library/struct.html
		# '<' (= little-endian)
		# 'I' unsigned int
		r += struct.pack("<I", length)
		r += struct.pack("<I", self.timestamp)
		r += struct.pack("<I", self.pos_x)
		r += struct.pack("<I", self.pos_y)
		r += struct.pack("<I", self.pos_z)
		r += struct.pack("<I", self.pitch)
		r += struct.pack("<I", self.yaw)
		r.append(self.flags1)
		r.append(self.flags2)
		r.append(ETX)

		return r

	def deserialize(self, data):
		self.timestamp = struct.unpack("<I", data[5:9])[0]
		self.pos_x = struct.unpack("<I", data[9:13])[0]
		self.pos_y = struct.unpack("<I", data[13:17])[0]
		self.pos_z = struct.unpack("<I", data[17:21])[0]
		self.pitch = struct.unpack("<I", data[21:25])[0]
		self.yaw = struct.unpack("<I", data[25:29])[0]
		self.flags1 = data[29]
		self.flags2 = data[30]

	def __str__(self):
		return "{:d} ({:d} {:d} {:d}) ({:d} {:d}) ({:08b} {:08b})".format(self.timestamp, self.pos_x, self.pos_y, self.pos_z, self.pitch, self.yaw, self.flags1, self.flags2)
