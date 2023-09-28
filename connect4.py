import numpy as np

def generate_winning_quadruplets(rows, cols):
    quadruplets = []
    for row in range(rows):
        for col in range(cols):
            if col <= cols - 4:
                quadruplets.append([(row, col + i) for i in range(4)])
            if row <= rows - 4:
                quadruplets.append([(row + i, col) for i in range(4)])
            if col <= cols - 4 and row <= rows - 4:
                quadruplets.append([(row + i, col + i) for i in range(4)])
            if col >= 3 and row <= rows - 4:
                quadruplets.append([(row + i, col - i) for i in range(4)])
    return quadruplets

class Connect4:
    def __init__(self, rows=6, cols=7):
        self.rows = rows
        self.cols = cols
        self.board = np.zeros((rows, cols), dtype=int)
        self.winning_quadruplets = generate_winning_quadruplets(rows, cols)
        
    def reset(self):
        self.board.fill(0)
    
    def set_board(self, board):
        self.board = board
        
    def has_won(self, player):
        for quad in self.winning_quadruplets:
            if all(self.board[x, y] == player for x, y in quad):
                return True
        return False

    def play(self, col, player):
        for row in reversed(range(self.rows)):
            if self.board[row, col] == 0:
                self.board[row, col] = player
                return True
        return False
    
    def is_finished(self):
        if any(self.has_won(player) for player in [1, -1]):
            return True
        if np.all(self.board != 0):
            return True
        return False

    def run(self, player1, player2):
        self.reset()
        moves = 0
        while not self.is_finished():
            for player in [player1, player2]:
                col = player.play(self.board)
                self.play(col, player.symbol)
                moves += 1
                if self.is_finished():
                    return player.symbol, moves