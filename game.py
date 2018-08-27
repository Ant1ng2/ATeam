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
