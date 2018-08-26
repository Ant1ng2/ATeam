class Game:

    def doMove(self, position, move):
        return position - move

    def generateMoves(self, position):
        return [x + 1 for x in range(2) if x + 1 <= position]

    def primitive(self, position):
        '''
        Get primitive value
        -1: lose; 1: win; 0: undecided
        '''
        if position == 0:
            return -1
        else:
            return 0

    def solve(self, position):
        for move in self.generateMoves(position):
            newPosition = self.doMove(position, move)
            primitiveValue = self.primitive(newPosition)
            if primitiveValue == -1 or (primitiveValue == 0 and self.solve(newPosition) == -1):
                return 1
        else:
            return -1

game = Game()
for i in range(11):
    print(i, game.solve(i))