import numpy as np
import random

class RandomPlayer:
    def __init__(self, symbol):
        self.symbol = symbol
    
    def play(self, board):
        valid_columns = np.where(board[0, :] == 0)[0]
        return random.choice(valid_columns)
    