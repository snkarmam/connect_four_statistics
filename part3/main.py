from levers import Levers
from random_pick import RandomPick
from greedy_pick import GreedyPick
from epsilon_greedy_pick import EpsilonGreedyPick
from ucb import Ucb

total_play_times = 1000000
amount_of_levers = 10
levers = Levers(amount_of_levers)
algo = RandomPick(total_play_times, levers)
algo2 = GreedyPick(total_play_times, levers, 100)
algo3 = EpsilonGreedyPick(total_play_times, levers, 100, 0.001, True)
algo4 = Ucb(total_play_times, levers)

result = algo.play()
result_2 = algo2.play()
result_3 = algo3.play()
result_4 = algo4.play()
print(result)
print(result_2)
print(result_3)
print(result_4)