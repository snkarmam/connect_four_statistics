import random

class RandomPick():
	def __init__(self, total_play_times, levers) -> None:
		self.total_play_times = total_play_times
		self.levers = levers
		self.amount_of_levers = len(self.levers.get_levers())

	def _choice(self):
		return random.randint(0, self.amount_of_levers-1)
	
	def play(self):
		self.picks = [0] * self.amount_of_levers
		gain = 0
		for _ in range(0, self.total_play_times):
			choice = self._choice()
			self.picks[choice] += 1
			gain  += self.levers.pick_lever(choice)
		return (self.picks, gain)
