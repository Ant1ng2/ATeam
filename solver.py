import game
class Solver:

    def solve(self, game):
        for move in game.generateMoves():
            newPosition = game.doMove(move)
            primitiveValue = game.primitive()
            if primitiveValue == -1 or (primitiveValue == 0 and self.solve(newPosition) == -1):
                return 1
        return -1

def solving(games):
    results = {}
    solver = Solver()
    for game in games:
        results[game.getState()] = solver.solve(game)
    return results

solver = Solver()
games = [game.Game(y) for y in range(11)]
solved = solving(games)
for key in solved.keys():
    print [key, solved[key]]
