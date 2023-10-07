import random

class RandomPick():
	def __init__(self, t, levers, n) -> None:
		self.t = t
		self.levers = levers
		self.n = n

	def _choice(self):
		return random.randint(0, self.n-1)
	
	def play(self):
		self.picks = [0] * self.n
		gain = 0
		for _ in range(0, self.t):
			choice = self._choice()
			print(choice)
			self.picks[choice] += 1
			gain  += self.levers.pick_lever(choice)
		return (self.picks, gain)
