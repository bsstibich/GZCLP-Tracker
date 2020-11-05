class Lift():
	def __init__(self, name = "", tier = 1, sets = 5, reps = 3, weight = 25, prog = 5):

		self._name = name
		self._tier = tier
		self._sets = sets
		self._reps = reps

		self._weight = weight

		self._prog = prog

	def prog_reprange(self):
		if self._sets == 5:
			self._sets = 6
			self._reps = 2
		elif self._sets == 6:
			self._sets = 10
			self._reps = 1
		elif self._sets == 10:
			self._weight = (int(input('What would you like your new working weight to be? ')))
			self._sets = 5
			self._reps = 3
			print(f'\nNext time you do this exercise you\'ll do {self._sets} sets of {self._reps} reps at {self._weight} lbs.')
		elif self._sets == 3 and self._reps == 10:
			self._reps = 8
		elif self._sets == 3 and self._reps == 8:
			self._reps = 6
		elif self._sets == 3 and self._reps == 6:
			self._weight = (int(input('\nWhat would you like your new working weight to be? ')))
			self._sets = 3
			self._reps = 10
			print(f'\nNext time you do this exercise you\'ll do {self._sets} sets of {self._reps} reps at {self._weight} lbs.')


