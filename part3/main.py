from levers import Levers
from random_pick import RandomPick

t = 10
amount_of_levers = 10
levers = Levers(amount_of_levers)
algo = RandomPick(t, levers, amount_of_levers)
result = algo.play()
print(result)