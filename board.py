
class Board:
    def __init__(self):
        self.image = ""
        rows, cols = (8,8)
        self.board = [[0 for i in range(cols)] for j in range(rows)]
        self.initialBoard()

    def initialBoard(self):
        self.board = [['rw', 'nw', 'bw', 'kw', 'qw', 'bw', 'nw', 'rw'],
                      ['pw', 'pw', 'pw', 'pw', 'pw', 'pw', 'pw', 'pw'],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
                      ['r', 'n', 'b', 'k', 'q', 'b', 'n', 'r']]
