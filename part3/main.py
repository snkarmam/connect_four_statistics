from levers import Levers
from random_pick import RandomPick
from greedy_pick import GreedyPick
from epsilon_greedy_pick import EpsilonGreedyPick

t = 10000
amount_of_levers = 10
levers = Levers(amount_of_levers)
algo = RandomPick(t, levers, amount_of_levers)
algo2 = GreedyPick(t, levers, amount_of_levers, 100)
algo3 = EpsilonGreedyPick(t, levers, amount_of_levers, 100, 0.001, True)
result = algo.play()
result_2 = algo2.play()
result_3 = algo3.play()
print(result)
print(result_2)
print(result_3)