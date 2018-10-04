import game
class Solver:

    def solve(self, game):
        for move in game.generateMoves():
            newPosition = game.doMove(move)
            primitiveValue = game.primitive()
            if primitiveValue == -1 or (primitiveValue == 0 and self.solve(newPosition) == -1):
                return 1
        return -1
