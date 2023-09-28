import matplotlib.pyplot as plt
from connect4 import Connect4

class DistributionOfMoves():
	def __init__(self, num_trials, player1, player2) -> None:
		self.num_trials = num_trials
		self.player1 = player1
		self.player2 = player2


	def run(self):
		moves_distribution = {1: [], -1: []}
		
		for _ in range(self.num_trials):
			game = Connect4()
			winner, moves = game.run(self.player1, self.player2)
			moves_distribution[winner].append(moves)
			print("game " + str(_) +  " done, winner is " + str(winner) + " amount of moves: " + str(moves))

		self._show_result(moves_distribution)


	def _show_result(self, moves_distribution):
		print("Player 1 wins:", len(moves_distribution[1]))
		print("Player 2 wins:", len(moves_distribution[-1]))
		
		plt.hist(moves_distribution[1], alpha=0.5, label='Monte Carlo Player wins')
		plt.hist(moves_distribution[-1], alpha=0.5, label='Player 2 wins')
		plt.legend(loc='upper right')
		plt.xlabel('Number of moves')
		plt.ylabel('Frequency')
		plt.title('Distribution of number of moves before a win')
		plt.show()