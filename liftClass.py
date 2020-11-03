
class Lift():
	def __init__(self, name = "", tier = 1, sets = 5, reps = 3, weight = 25, prog = 5):

		self._name = name
		self._tier = tier
		self._sets = sets
		self._reps = reps

		self._weight = weight

		self._weight_progression = prog

#########################################Load and save Lifts, put in another class. Maybe the menu class
#with open('lifts.swole', 'wb') as file:
	#pickle.dump(lift, file)

#with open('lifts.swole', 'rb') as file:
	#lift = pickle.load(file)

