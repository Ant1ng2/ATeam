from game import Game

class OddEven(Game):

    def __init__(self):
        self.players = [0, 0]
        self.turn = 0
        self.remaining = 15

    def __init__(self, position):
        self.__init__()
        self.remaining = position

    def getState(self):
        return (self.playes[0], self.players[1], self.remaining)

    def doMove(self, move):
        if move % 2 == 1:
            self.players[self.turn % 2] = (self.players[self.turn % 2] + 1) % 2
        self.turn = (self.turn + 1) % 2

    def generateMoves(self):
        return [x + 1 for x in range(3) if x + 1 <= self.remaining]

    def primitive(self):
        "Assume persepective of Player 1"
        if self.turn % 2 == 0 and self.remaining = 0:
            return -1
        if self.turn % 2 == 1 and self.remaining = 0:
            return 1
        else:
            return 0
