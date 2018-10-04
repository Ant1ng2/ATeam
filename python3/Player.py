import Game
import Solver
import random

class Player():
	
	def solve(self, game):
		solver = Solver.Solver()
		solver.solve(game)
		self.memory = solver.memory

	def printWrongMove(self):
		if len(self.wrongMove) == 0:
			print("No wrong move")
		else:
			print("Wrong move:")
			for item in self.wrongMove:
				print("Player {} made wrong move {} in step {}, status from {} become {}. Correct move is {}".format(item[0], item[1], item[2], item[3], item[4], item[5]))

	def findCorrectMove(self, game, validMove):
		if self.memory[game.serialize()] == Game.Value.Lose:
			return validMove
		else:
			correctMove = []
			for move in validMove:
				newGame = game.doMove(move)
				if self.memory[newGame.serialize()] == Game.Value.Lose:
					correctMove.append(move)
			return correctMove


	def play(self, game, computer=True):
		self.solve(game)
		self.wrongMove = []
		print("Game name:", game.gameName())
		player = 1
		step = 0

		while game.primitive() == Game.Value.Undecided:
			step += 1
			validMove = game.generateMoves()
			print()
			print("Status:", game.status())
			print("Valid move:", validMove)

			if not computer or player == 1:

				while True:
					move = input("Player {} move in step {}: ".format(player, step))
					if move.isdigit() and int(move) in validMove:
						move = int(move)
						break
					else:
						print("Wrong input")

			correctMove = self.findCorrectMove(game, validMove)
			if not computer or player == 1:
				if move not in correctMove:
					self.wrongMove.append([player, move, step, game.status()])
					game = game.doMove(move)
					self.wrongMove[-1].append(game.status())
					self.wrongMove[-1].append(correctMove)
				else:
					game = game.doMove(move)
			else:
				move = random.choice(correctMove)
				print("Computer move in step {}: {}".format(step, move))
				game = game.doMove(move)

			player = player%2+1

		print()
		print("Game End")
		if game.primitive() == Game.Value.Lose:
			if player%2+1 == 2 and computer:
				print("Winner: Computer")
			else:
				print("Winner: Player", player%2+1)
		else:
			if player == 2 and computer:
				print("Winner: Computer")
			else:
				print("Winner: Player", player)
		print()
		self.printWrongMove()


player = Player()
player.play(Game.OddEven(15))