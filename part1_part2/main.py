from random_player import RandomPlayer
from monte_carlo_player import MonteCarloPlayer
from distribution_of_moves import DistributionOfMoves

if __name__ == "__main__":
    player2 = MonteCarloPlayer(-1, 1, 1)
  #  player2 = RandomPlayer(-1)
    player1 = MonteCarloPlayer(1, -1, 1)
    #player2 = RandomPlayer(-1)
    runner = DistributionOfMoves(100, player1, player2)
    runner.run()
