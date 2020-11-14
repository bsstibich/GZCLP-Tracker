import pickle

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
			print("It seems you've set a custom reprange, so automatic progression is not an option. ")

	def change_weight(self):
		new_weight = int(input(f'\nYour current weight for {self._name} is {self._weight}.\nWhat would you like your new working weight to be '))
		self._weight = new_weight
		full_lifts = self.load()
		full_lifts[str(self._tier)][self._name]._weight = new_weight
		self.save(full_lifts)

	def change_reprange(self):
		new_sets = int(input(f'\nYour current reprange for {self._name} is {self._sets} sets of {self._reps} reps.\nHow many sets of would you like to start doing? '))
		new_reps = int(input('\nHow many reps would you like to do in each set?'))
		self._reps = new_reps
		self._sets = new_sets
		full_lifts = self.load()
		full_lifts[str(self._tier)][self._name]._reps = new_reps
		full_lifts[str(self._tier)][self._name]._sets = new_sets
		self.save(full_lifts)
	

	def plate_picker(self):
		full_weights = self.load()
		weight = self._weight - (full_weights['bar'])
		plates = {"45":0, "35":0, "25":0, "10":0, "5":0,"2.5":0}
		
		while weight > 0:
			if weight >= 90:
				plates["45"] += 1
				weight -= 90
				pass
			elif weight >= 70:
				plates["35"] += 1
				weight -= 70
				pass
			elif weight >= 50:
				plates["25"] += 1
				weight -= 50
				pass
			elif weight >= 20:
				plates["10"] += 1
				weight -= 20
				pass
			elif weight >= 10:
				plates["5"] += 1
				weight -= 10
				pass
			elif weight >=5:
				plates["2.5"] += 1
				weight -= 5
				pass
		print(plates)



	def load(self):
		with open('lifts.swole', 'rb') as file: #load
			full_lifts = pickle.load(file)
		return full_lifts

	def save(self,full_lifts):
		with open('lifts.swole', 'wb') as file: #save
			pickle.dump(full_lifts, file)



