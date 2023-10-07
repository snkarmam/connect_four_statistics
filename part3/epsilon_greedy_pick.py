from greedy_pick import GreedyPick
import random

class EpsilonGreedyPick():
	def __init__(self, t, levers, amount_of_levers, greed, epsilon, premilinary_exploration) -> None:
		self.t = t
		self.levers = levers
		self.amount_of_levers = amount_of_levers
		self.greed = greed
		self.epsilon = epsilon
		self.premilinary_exploration = premilinary_exploration

	def _explore(self):
		greedy_pick = GreedyPick(self.t, self.levers, self.amount_of_levers, self.greed)
		return greedy_pick.explore()

	def _pick_random_choice(self):
		choice = random.randint(0, self.amount_of_levers-1)
		result_of_choice = self.levers.pick_lever(choice)
		self.gain += result_of_choice
		self._calculate_new_average_and_amount(choice, result_of_choice)

	def _pick_best_choice(self):
		best_pick = self.average_return_per_lever.index(max(self.average_return_per_lever))
		result_of_choice = self.levers.pick_lever(best_pick)
		self.gain += result_of_choice
		self._calculate_new_average_and_amount(best_pick, result_of_choice)

	def play(self):
		self.average_return_per_lever = [0] * self.amount_of_levers
		self.amount_of_plays_per_lever = [0] * self.amount_of_levers
		self.gain = 0
		if self.premilinary_exploration:
			self.average_return_per_lever = self._explore()
			self.amount_of_plays_per_lever = [self.greed] * self.amount_of_levers
		for _ in range(0, self.t):
			random_chance = random.uniform(0, 1)
			if random_chance <= self.epsilon:
				self._pick_random_choice()
			else:
				self._pick_best_choice()
		return (self.amount_of_plays_per_lever, self.gain)

	def _calculate_new_average_and_amount(self, choice, result):
		new_average = (self.average_return_per_lever[choice] * self.amount_of_plays_per_lever[choice] + result)/(self.amount_of_plays_per_lever[choice] + 1)
		self.average_return_per_lever[choice] = new_average
		self.amount_of_plays_per_lever[choice] += 1

	