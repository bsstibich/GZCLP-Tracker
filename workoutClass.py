from liftClass import Lift
import pickle

class Workout():
	def __init__(self, t1 = False, t2 = False, day = 1):
		self._t1 = t1
		self._t2 = t2
		self._day = day

	def session(self, lift): #works for both tier 1 and tier 2 lifts
		setCounter = 1
		print(f"\nWorkout Day {self._day}:\n==============\nLets do tier {lift._tier} {lift._name}! Do {lift._sets} sets of {lift._reps} reps at {lift._weight} lbs.")
		while setCounter <= lift._sets: #loop to repeat set checker until sets are complete 
			inp = input(f'\nWere you able to finish set {setCounter}? (Y/N)  ') 
			if setCounter == lift._sets and inp.lower() == 'y': #ends loop and workout
				lift._weight += lift._prog
				print(f'\nGreat Job! Next time you do this exercise you\'ll do {lift._sets} sets of {lift._reps} reps at {lift._weight} lbs.')
				break
			elif inp.lower() == 'y':
				setCounter += 1
			elif inp.lower() == 'n':
				inp = input('\nDon\'t sweat it! Would you like to adjust your rep-range? (Y/N) ')
				if inp.lower() == 'y':
					lift.fail_lift()
					break
			else:
				print('\n\'Ey don\'t do dat.')
			
		self.save(lift)



	def save(self, lift):
		with open('lifts.swole', 'rb') as file: #load
			full_lifts = pickle.load(file)

		full_lifts[str(lift._tier)][lift._name] = lift #remake

		with open('lifts.swole', 'wb') as file: #save
			pickle.dump(full_lifts, file)



