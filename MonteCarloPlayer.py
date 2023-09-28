import numpy as np
from Connect4 import Connect4
from RandomPlayer import RandomPlayer

class MonteCarloPlayer():
    def __init__(self,symbol, adversary_symbol, simulation_amount) -> None:
        self.symbol = symbol
        self.adversary_symbol = adversary_symbol
        self.simulation_amount = simulation_amount
    
    def play(self, board):
        valid_columns = np.where(board[0, :] == 0)[0]
        average_for_moves = {}
        for move in valid_columns:
            average_for_moves[move] = self.run_simulation(move, np.copy(board))
        return self.largest_average(average_for_moves)

    def largest_average(self, average_for_moves):
        largest_average = -1
        best_move = -1
        for move in average_for_moves:
            if average_for_moves[move] > largest_average:
                best_move = move
                largest_average = average_for_moves[move]
        return best_move
        
    def run_simulation(self, move, board_copy):
        game = Connect4()
        game.set_board(board_copy)
        game.play(move, self.symbol)
        averages = []
        for _ in range(0, self.simulation_amount):
            averages.append(game.run(RandomPlayer(self.adversary_symbol), RandomPlayer(self.symbol))[0])
        average_for_move = sum(averages)/len(averages)
        return average_for_move
