import numpy as np

from RandomPlayer import RandomPlayer
from MonteCarloPlayer import MonteCarloPlayer
from DistributionOfMoves import DistributionOfMoves

if __name__ == "__main__":
    player1 = MonteCarloPlayer(1, -1, 10)
    player2 = RandomPlayer(-1)
    runner = DistributionOfMoves(30, player1, player2)
    runner.run()
