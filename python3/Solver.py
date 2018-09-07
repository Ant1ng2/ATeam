import Game

class Solver():

	def __init__(self):
		self.memory = {}

	def resetMemory(self):
		self.memory.clear()

	def solveWithoutMemory(self, game):
		primitive = game.primitive()
		if primitive != Game.Value.Undecided:
			return primitive
		for move in game.generateMoves():
			newGame = game.doMove(move)
			if self.solve(newGame) == Game.Value.Lose:
				return Game.Value.Win # Not necessarily traverse all subtree
		return Game.Value.Lose

	# this one will end when find the anther is Win
	def solve(self, game): 
		serialized = game.serialize()
		if serialized in self.memory:
			return self.memory[serialized]
		primitive = game.primitive()
		if primitive != Game.Value.Undecided:
			self.memory[serialized] = primitive
			return primitive
		for move in game.generateMoves():
			newGame = game.doMove(move)
			if self.solve(newGame) == Game.Value.Lose:
				self.memory[serialized] = Game.Value.Win
				return Game.Value.Win # Not necessarily traverse all subtree
		self.memory[serialized] = Game.Value.Lose
		return Game.Value.Lose

		# this one will traverse all subtree
	def solveTraverse(self, game): 
		winFlag = False
		serialized = game.serialize()
		if serialized in self.memory:
			return self.memory[serialized]
		primitive = game.primitive()
		if primitive != Game.Value.Undecided:
			self.memory[serialized] = primitive
			return primitive
		for move in game.generateMoves():
			newGame = game.doMove(move)
			if self.solve(newGame) == Game.Value.Lose:
				self.memory[serialized] = Game.Value.Win
				winFlag = True
		if not winFlag:
			self.memory[serialized] = Game.Value.Lose
		return Game.Value.Win if winFlag else Game.Value.Lose

solver = Solver()

#print(solver.solve(Game.Nim(10)))
print(solver.solveTraverse(Game.OddEven(15)))

memory = []
for game, value in solver.memory.items():
	memory.append((game, value))
	
memory.sort(key=lambda item: int(item[0].split()[0]), reverse=True)
for item in memory:
	print(item[0], item[1])


