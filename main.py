import numpy as np

from random_player import RandomPlayer
from monte_carlo_player import MonteCarloPlayer
from distribution_of_moves import DistributionOfMoves
from random_player import RandomPlayer

if __name__ == "__main__":
    player1 = MonteCarloPlayer(1, -1, 10)
    player2 = RandomPlayer(-1)
    runner = DistributionOfMoves(30, player1, player2)
    runner.run()
