"""import solver"""
class Game:

    def __init__(self):
        self.position = 10

    def __init__(self, position):
        self.position = position

    def getState(self):
        return self.position

    def doMove(self, move):
        return Game(self.position - move)

    def generateMoves(self):
        return [x + 1 for x in range(2) if x + 1 <= self.position]

    def primitive(self):
        '''
        Get primitive value
        -1: lose; 1: win; 0: undecided
        '''
        if self.position == 0:
            return -1
        else:
            return 0

"""game = Game(10)
bot = solver.Solver()
player = input('Choose 1 to go first, 2 to go second: ')
while game.getState >= 0:
    if player == 1:
        if game.getState() <= 0:
            print 'You lose'
            break
        else:
            print 'Your move. Current position is ', game.getState()
            move = input('? ')
            game = game.doMove(move)
    else:
        if game.getState() <= 0:
            print 'You win'
            break
        else:
            botMove = bot.solve(game)
            print 'Computer chooses ', botMove
            game = game.doMove(botMove)
"""
