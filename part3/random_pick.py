import random

class RandomPick():
	def __init__(self, t, levers, amount_of_levers) -> None:
		self.t = t
		self.levers = levers
		self.amount_of_levers = amount_of_levers

	def _choice(self):
		return random.randint(0, self.amount_of_levers-1)
	
	def play(self):
		self.picks = [0] * self.amount_of_levers
		gain = 0
		for _ in range(0, self.t):
			choice = self._choice()
			self.picks[choice] += 1
			gain  += self.levers.pick_lever(choice)
		return (self.picks, gain)
