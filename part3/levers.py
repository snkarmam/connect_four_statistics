import random

class Levers():
	def __init__(self, n) -> None:
		self.levers = []
		self.picks = []
		for _ in range(0, n):
			self.levers.append(random.uniform(0, 1))
			self.picks.append(0)
		self.n = n

	def get_levers(self):
		return self.levers
	
	def pick_lever(self, choice):
		new_random_number = random.uniform(0, 1)
		if new_random_number <= self.levers[choice]:
			return 1
		return 0
