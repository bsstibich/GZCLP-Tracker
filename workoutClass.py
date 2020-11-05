from liftClass import Lift
import pickle

class Workout():
	def __init__(self, t1, t2):
		self._t1 = t1
		self._t2 = t2

	def session(self, lift):
		setCounter = 1
		print(f"\nWorkout Day 1:\n==============\nLets start with Tier {lift._tier} {lift._name}! Do {lift._sets} sets of {lift._reps} reps at {lift._weight} lbs.")
		while setCounter <= lift._sets:
			inp = input(f'\nWere you able to finish set {setCounter}? (Y/N)  ') 
			if setCounter == lift._sets and inp.lower() == 'y':
				lift._weight += lift._prog
				print(f'\nGreat Job! Next time you do this exercise you\'ll do {lift._sets} sets of {lift._reps} reps at {lift._weight} lbs.')
			elif inp.lower() == 'y':
				print("nice")
			elif inp.lower() == 'n':
				inp = input('\nDon\'t sweat it! Would you like to adjust your rep-range? (Y/N) ')
				if inp.lower() == 'y':
					print('yeet') #prog_reprange()
			else:
				print('\nInvalid Input')
			setCounter += 1
		self.save(lift)

	def save(self, lift):
		with open('lifts.swole', 'rb') as file: #load
			full_lifts = pickle.load(file)

		full_lifts[str(lift._tier)][lift._name] = lift

		with open('lifts.swole', 'wb') as file: #save
			pickle.dump(full_lifts, file)


with open('lifts.swole', 'rb') as file:
	lifts = pickle.load(file)
print(lifts['2']['Squat']._weight)
workout = Workout(lifts['1']['Squat'], lifts['2']['Bench Press'])
workout.session(workout._t2)
