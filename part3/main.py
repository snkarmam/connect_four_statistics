from levers import Levers
from random_pick import RandomPick

t = 10
n = 10
levers = Levers(n)
algo = RandomPick(t, levers, n)
result = algo.play()
print(result)