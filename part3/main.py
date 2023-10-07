from levers import Levers
from random_pick import RandomPick
from greedy_pick import GreedyPick

t = 10
amount_of_levers = 10
levers = Levers(amount_of_levers)
algo = RandomPick(t, levers, amount_of_levers)
algo2 = GreedyPick(t, levers, amount_of_levers, 20)
result = algo.play()
result_2 = algo2.play()
print(result)
print(result_2)