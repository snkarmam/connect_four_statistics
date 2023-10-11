from levers import Levers
from random_pick import RandomPick
from greedy_pick import GreedyPick
from epsilon_greedy_pick import EpsilonGreedyPick
from ucb import Ucb
import matplotlib.pyplot as plt

total_play_times = 100000
amount_of_levers = 20
levers = Levers(amount_of_levers)
algo = RandomPick(total_play_times, levers)
algo2 = GreedyPick(total_play_times, levers, 1000)
algo3 = EpsilonGreedyPick(total_play_times, levers, 100, 0.1, True)
algo4 = Ucb(total_play_times, levers)

result = algo.play()
result_2 = algo2.play()
result_3 = algo3.play()
result_4 = algo4.play()
print(result)
print(result_2)
print(result_3)
print(result_4)

algorithms = ['RandomPick', 'GreedyPick', 'EpsilonGreedyPick', 'Ucb']
gains = [result[1], result_2[1], result_3[1], result_4[1]]

plt.figure(figsize=(10, 6))
plt.bar(algorithms, gains, color=['blue', 'green', 'red', 'purple'])
plt.xlabel('Algorithm')
plt.ylabel('Total Gain')
plt.title('Total Gains by Algorithm')
plt.show()
