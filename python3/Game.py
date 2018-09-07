from enum import Enum

class Value(Enum):
	Win = "Win"
	Lose = "Lose"
	Undecided = "Undecided"


class Nim():
	# Each instance has its own status
	# In this game, (position) is the status

	def __init__(self, position):
		self.position = position

	def doMove(self, move):
		return Nim(self.position - move)

	def generateMoves(self):
		return [x + 1 for x in range(2) if x + 1 <= self.position]

	def primitive(self):
		if self.position == 0:
			return Value.Lose
		else:
			return Value.Undecided

	def serialize(self):
		return "{}".format(self.position)

	def deserialize(serializedString):
		status = serializedString.split()
		return Nim(status[0])


class OddEven():
	# Each instance has its own status
	# In this game, (position, lParity, rParity) is the status

	def __init__(self, position, lParity = 0, rParity = 0):
		self.position = position
		self.lParity = lParity
		self.rParity = rParity

	def doMove(self, move):
		return OddEven(self.position - move, self.rParity, (self.lParity+move)%2)

	def generateMoves(self):
		return [x + 1 for x in range(3) if x + 1 <= self.position]

	def primitive(self):
		if self.position != 0:
			return Value.Undecided
		elif self.lParity == 0:
			return Value.Win
		else:
			return Value.Lose

	def serialize(self):
		return "{} {} {}".format(self.position, self.lParity, self.rParity) 

	def deserialize(serializedString):
		status = serializedString.split()
		return Nim(status[0], status[1], status[2])