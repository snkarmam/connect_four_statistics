import numpy as np
from connect4 import Connect4
from random_player import RandomPlayer

class MonteCarloPlayer():
    def __init__(self,symbol, adversary_symbol, simulation_amount):
        self.symbol = symbol
        self.adversary_symbol = adversary_symbol
        self.simulation_amount = simulation_amount
    
    def play(self, board):
        valid_columns = np.where(board[0, :] == 0)[0]
        average_for_moves = {}
        for move in valid_columns:
            average_for_moves[move] = self._run_simulation(move, np.copy(board))
        return self._best_possible_move(average_for_moves)

    def _best_possible_move(self, average_for_moves):
        if self.symbol == 1:
            return self._highest_average(average_for_moves)
        else:
            return self._lowest_average(average_for_moves)
    
    def _highest_average(self, average_for_moves):
        largest_average = -1
        best_move = -1
        for move in average_for_moves:
            if average_for_moves[move] > largest_average:
                best_move = move
                largest_average = average_for_moves[move]
        return best_move
    
    def _lowest_average(self, average_for_moves):
        lowest_average = 1
        best_move = -1
        for move in average_for_moves:
            if average_for_moves[move] < lowest_average:
                best_move = move
                lowest_average = average_for_moves[move]
        return best_move
        
    def _run_simulation(self, move, board_copy):
        game = Connect4()
        averages = []
        for _ in range(0, self.simulation_amount):
            game.set_board(np.copy(board_copy))
            game.play(move, self.symbol)
            averages.append(game.run_once(RandomPlayer(self.adversary_symbol), RandomPlayer(self.symbol))[0])
        average_for_move = sum(averages)/len(averages)
        return average_for_move