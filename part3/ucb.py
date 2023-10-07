import math

class Ucb():
	def __init__(self, total_play_times, levers) -> None:
		self.total_play_times = total_play_times
		self.levers = levers
		self.amount_of_levers = len(self.levers.get_levers())
		self.average_return_per_lever = [0] * self.amount_of_levers
		self.amount_of_plays_per_lever = [0] * self.amount_of_levers
		self.gain = 0

	def play(self):
		self.turns_taken = 0
		for _ in range(0, self.total_play_times):
			self.turns_taken += 1
			choice = self._calculate_choice()
			self._play_lever(choice)
		return (self.amount_of_plays_per_lever, self.gain)
	
	def _play_lever(self, choice):
		result_of_action = self.levers.pick_lever(choice)
		self.gain += result_of_action
		self._calculate_new_average_and_amount(choice, result_of_action)

	def _calculate_new_average_and_amount(self, choice, result):
		new_average = (self.average_return_per_lever[choice] * self.amount_of_plays_per_lever[choice] + result)/(self.amount_of_plays_per_lever[choice] + 1)
		self.average_return_per_lever[choice] = new_average
		self.amount_of_plays_per_lever[choice] += 1

	def _calculate_choice(self):
		weights_for_actions = []
		for option in range(0, self.amount_of_levers):
			self.amount_of_plays_per_lever[option]
			if self.amount_of_plays_per_lever[option] == 0:
				weight_for_action = 10000000
			else:
				weight_for_action = self.average_return_per_lever[option] + math.sqrt((2*math.log(self.turns_taken)/self.amount_of_plays_per_lever[option]))
			weights_for_actions.append(weight_for_action)
		return weights_for_actions.index(max(weights_for_actions))
