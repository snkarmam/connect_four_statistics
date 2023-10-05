import matplotlib.pyplot as plt
from connect4 import Connect4

class DistributionOfMoves():
	def __init__(self, num_trials, player1, player2) -> None:
		self.num_trials = num_trials
		self.player1 = player1
		self.player2 = player2


	def run(self):
		moves_distribution = {1: [], -1: []}
		
		game = Connect4()
		results = game.run_multiple_times(self.player1, self.player2, self.num_trials)
		for tuple in results:
			moves_distribution[tuple[0]].append(tuple[1])
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