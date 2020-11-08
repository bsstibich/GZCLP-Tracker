
class Lift():
	def __init__(self, name = "", tier = 1, sets = 5, reps = 3, weight = 25, prog = 5):

		self._name = name
		self._tier = tier
		self._sets = sets
		self._reps = reps

		self._weight = weight

		self._prog = prog

	def fail_lift(self):
		if self._sets == 5:
			self._sets = 6
			self._reps = 2
		elif self._sets == 6:
			self._sets = 10
			self._reps = 1
		elif self._sets == 10:
			self.change_weight()
			self._sets = 5
			self._reps = 3
			print(f'\nNext time you do this exercise you\'ll do {self._sets} sets of {self._reps} reps at {self._weight} lbs.')
		elif self._sets == 3 and self._reps == 10:
			self._reps = 8
		elif self._sets == 3 and self._reps == 8:
			self._reps = 6
		elif self._sets == 3 and self._reps == 6:
			self.change_weight()
			self._sets = 3
			self._reps = 10
			print(f'\nNext time you do this exercise you\'ll do {self._sets} sets of {self._reps} reps at {self._weight} lbs.')
		else:
			print("It seems you've set a custome reprange, so automatic progression is not an option.")

	def change_weight(self):
		new_weight = int(input(f'\nYour current weight for {self._name} is {self._weight}. What would you like your new working weight to be'))
		self._weight = new_weight
		#save?

	def change_reprange(self):
		new_sets = int(input(f'\nYour current reprange for {self._name} is {self._sets} sets of {self._reps} reps. How many sets of would you like to start doing?'))
		new_reps = int(input('\nHow many reps would you like to do in each set?'))
		self._reps = new_reps
		self._sets = new_sets
		#save?




