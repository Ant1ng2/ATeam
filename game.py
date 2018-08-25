class Game:

    def __init__(self):
        self.position = 10

    def setPosition(self, position):
        self.position = position

    def doMove(self, move):
        self.position = self.position - move

    def generateMoves(self):
        return [x + 1 for x in range(2) if x + 1 <= self.position]

    def primative(self):
        if self.position == 0:
            return -1
        if self.position == 1:
            return 1
        else:
            return 0
