import game
class Solver:

    def solve(self, game):
        for move in game.generateMoves():
            newPosition = game.doMove(move)
            primitiveValue = game.primitive()
            if primitiveValue == -1 or (primitiveValue == 0 and self.solve(newPosition) == -1):
                return 1
        else:
            return -1

solver = Solver()
for y in range(11):
    game2 = game.Game(y)
    print (y, solver.solve(game2))
