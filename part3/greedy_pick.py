class GreedyPick():
	def __init__(self, t, levers, amount_of_levers, greed) -> None:
		self.t = t
		self.levers = levers
		self.amount_of_levers = amount_of_levers
		self.greed = greed
		self.gain = 0

	def explore(self):
		average_return_per_lever = []
		print(self.greed//self.amount_of_levers)
		for lever in range(0, self.amount_of_levers):
			average_return_per_lever.append(self._explore_lever(lever))
		return average_return_per_lever
	
	def _explore_lever(self, lever):
		return_for_lever = 0
		for _ in range(0, self.greed//self.amount_of_levers):
			return_for_lever += self.levers.pick_lever(lever)
		self.gain += return_for_lever
		average_return_for_lever = return_for_lever/self.greed
		return average_return_for_lever

	def play(self):
		self.gain = 0
		self.picks = [self.greed//self.amount_of_levers] * self.amount_of_levers
		exploration_results = self.explore()
		best_pick = exploration_results.index(max(exploration_results))
		self.picks[best_pick] = self.t - self.greed + self.greed//self.amount_of_levers
		for _ in range(self.greed, self.t):
			self.gain += self.levers.pick_lever(best_pick)
		return (self.picks, self.gain)
