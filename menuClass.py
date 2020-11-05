from liftClass import Lift
from workoutClass import Workout
import pickle

class Menu():
	def __init__(self):
		self.yeet = 0

	def run(self):
		with open('lifts.swole', 'rb') as file:
			lifts = pickle.load(file)
		run = 0
		while run == 0:
			print("\nWelcome to GZCLP tracker!\n0. Close Program\n1. Start Workout Day 1 (Tier 1 Squat, Tier 2 Bench Press)\n2. Start Workout Day 2 (Tier 1 Overhead Press, Tier 2 Deadlift)\n3. Start Workout Day 3 (Tier 1 Bench Press, Tier 2 Squat)\n4. Start Workout Day 4 (Tier 1 Deadlift, Tier 2 Overhead Press)\n5. Print Lifts\n6. Settings")
			ans = input("\nWhat would you like to do? ")
			if ans=='0':
				run = 99
			elif ans=='1':
				workout = Workout(lifts['1']['Squat'], lifts['2']['Bench Press'],1)
				workout.session(workout._t1)
				workout.session(workout._t2)
			elif ans=='2':
				workout = Workout(lifts['1']['Overhead Press'], lifts['2']['Row'],2)
				workout.session(workout._t1)
				workout.session(workout._t2)
			elif ans=='3':
				workout = Workout(lifts['1']['Bench Press'], lifts['2']['Squat'],3)
				workout.session(workout._t1)
				workout.session(workout._t2)
			elif ans=='4':
				workout = Workout(lifts['1']['Row'], lifts['2']['Overhead Press'],4)
				workout.session(workout._t1)
				workout.session(workout._t2)
			elif ans=='5':
				print(f"\nTier 1 Squat {lifts['1']['Squat']._weight} lbs reprange {lifts['1']['Squat']._sets}x{lifts['1']['Squat']._reps}")
				print(f"Tier 1 Overhead Press {lifts['1']['Overhead Press']._weight} lbs rep range {lifts['1']['Overhead Press']._sets}x{lifts['1']['Overhead Press']._reps}")
				print(f"Tier 1 Bench Press {lifts['1']['Bench Press']._weight} lbs rep range {lifts['1']['Bench Press']._sets}x{lifts['1']['Bench Press']._reps}")
				print(f"Tier 1 Deadlift {lifts['1']['Deadlift']._weight} lbs reprange {lifts['1']['Deadlift']._sets}x{lifts['1']['Deadlift']._reps}")
				print(f"\nTier 2 Squat {lifts['2']['Squat']._weight} lbs reprange {lifts['2']['Squat']._sets}x{lifts['2']['Squat']._reps}")
				print(f"Tier 2 Overhead Press {lifts['2']['Overhead Press']._weight} lbs reprange {lifts['2']['Overhead Press']._sets}x{lifts['2']['Overhead Press']._reps}")
				print(f"Tier 2 Bench Press {lifts['2']['Bench Press']._weight} lbs reprange {lifts['2']['Bench Press']._sets}x{lifts['2']['Bench Press']._reps}")
				print(f"Tier 2 Deadlifts {lifts['2']['Deadlift']._weight} lbs reprange {lifts['2']['Deadlift']._sets}x{lifts['2']['Deadlift']._reps}")
			elif ans=='6':
				print("\nSetting go here")
			else:
				print("Invalid Input")	
