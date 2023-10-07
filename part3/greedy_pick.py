from random_pick import RandomPick
class GreedyPick():
	def __init__(self, t, levers, amount_of_levers, greed) -> None:
		self.t = t
		self.levers = levers
		self.amount_of_levers = amount_of_levers
		self.greed = greed

	def _explore(self):
		average_return_per_lever = []
		for lever in range(0, self.amount_of_levers):
			average_return_per_lever.append(self._explore_lever(lever))
		return average_return_per_lever
	
	def _explore_lever(self, lever):
		return_for_lever = 0
		for _ in range(0, self.greed):
			return_for_lever += self.levers.pick_lever(lever)
		average_return_for_lever = return_for_lever/self.greed
		return average_return_for_lever


	def play(self):
		self.picks = [0] * self.amount_of_levers
		exploration_results = self._explore()
		best_pick = exploration_results.index(max(exploration_results))
		self.picks[best_pick] = self.t
		gain = 0
		for _ in range(0, self.t):
			gain += self.levers.pick_lever(best_pick)
		return (self.picks, gain)
