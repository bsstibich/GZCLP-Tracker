from liftClass import Lift
from workoutClass import Workout
import pickle
from os import system, name


class Menu():
	def __init__(self):
		self.yeet = 0

	def clear(self): 						 
	    if name == 'nt': # for windows
	        _ = system('cls')  
	    else: # for mac and linux
	        _ = system('clear') 
  
	def run(self):
		with open('lifts.swole', 'rb') as file:
			lifts = pickle.load(file)
		run = 0
		while run == 0:
			self.clear() 
			print("\nWelcome to GZCLP tracker!\n=========================\n0. Close Program\n1. Start Workout Day 1 (Tier 1 Squat, Tier 2 Bench Press)\n2. Start Workout Day 2 (Tier 1 Overhead Press, Tier 2 Deadlift)\n3. Start Workout Day 3 (Tier 1 Bench Press, Tier 2 Squat)\n4. Start Workout Day 4 (Tier 1 Deadlift, Tier 2 Overhead Press)\n5. Print Lifts\n6. Settings")
			ans = input("\nWhat would you like to do? ")
			if ans=='0':
				run = 99
			elif ans=='1':
				self.clear()
				workout = Workout(lifts['1']['Squat'], lifts['2']['Bench Press'],1)
				workout.session(workout._t1)
				workout.session(workout._t2)
			elif ans=='2':
				self.clear()
				workout = Workout(lifts['1']['Overhead Press'], lifts['2']['Row'],2)
				workout.session(workout._t1)
				workout.session(workout._t2)
			elif ans=='3':
				self.clear()
				workout = Workout(lifts['1']['Bench Press'], lifts['2']['Squat'],3)
				workout.session(workout._t1)
				workout.session(workout._t2)
			elif ans=='4':
				self.clear()
				workout = Workout(lifts['1']['Row'], lifts['2']['Overhead Press'],4)
				workout.session(workout._t1)
				workout.session(workout._t2)
			elif ans=='5': #find way to make display despite the clear() in the main menu
				self.clear()
				print(f"\nTier 1 Squat {lifts['1']['Squat']._weight} lbs reprange {lifts['1']['Squat']._sets}x{lifts['1']['Squat']._reps}")
				print(f"Tier 1 Overhead Press {lifts['1']['Overhead Press']._weight} lbs rep range {lifts['1']['Overhead Press']._sets}x{lifts['1']['Overhead Press']._reps}")
				print(f"Tier 1 Bench Press {lifts['1']['Bench Press']._weight} lbs rep range {lifts['1']['Bench Press']._sets}x{lifts['1']['Bench Press']._reps}")
				print(f"Tier 1 Deadlift {lifts['1']['Deadlift']._weight} lbs reprange {lifts['1']['Deadlift']._sets}x{lifts['1']['Deadlift']._reps}")
				print(f"\nTier 2 Squat {lifts['2']['Squat']._weight} lbs reprange {lifts['2']['Squat']._sets}x{lifts['2']['Squat']._reps}")
				print(f"Tier 2 Overhead Press {lifts['2']['Overhead Press']._weight} lbs reprange {lifts['2']['Overhead Press']._sets}x{lifts['2']['Overhead Press']._reps}")
				print(f"Tier 2 Bench Press {lifts['2']['Bench Press']._weight} lbs reprange {lifts['2']['Bench Press']._sets}x{lifts['2']['Bench Press']._reps}")
				print(f"Tier 2 Deadlifts {lifts['2']['Deadlift']._weight} lbs reprange {lifts['2']['Deadlift']._sets}x{lifts['2']['Deadlift']._reps}")
			elif ans=='6':
				settings = 0
				while settings == 0:
					self.clear()
					print("\nSettings Menu\n=============\nWhat would you like to change?\n0. Return to previous menu\n1. Change weight of a lift\n2. Change reprange of a lift")
					ans2 = input("\nWhat would you like to do? ")
					if ans2 == '0':
						break
					#Change Weights
					elif ans2 == '1':
						self.clear()
						print("\nWhat lift's weight would you like to change?\n============================================\n0. Return to previous menu\n1. Squat\n2. Bench Press\n3. Overhead Press\n4. Deadlift\n5. Barbell Rows\n")
						ans3 = input("What would you like to do? ")
						if ans3 == '0':
							break
						elif ans3 == '1':
							ans4 = input("Tier 1 or 2? ")
							if ans4 == '1':
								pass
								#changeweight t1 squat
							elif ans4 == '2':
								pass
								#changeweight t2 squat
							else:
								print("Invalid Input")
						elif ans3 == '2':
							ans4 = input("Tier 1 or 2? ")
							if ans4 == '1':
								pass
								#changeweight t1 bench
							elif ans4 == '2':
								pass
								#changeweight t2 bench
							else:
								print("Invalid Input")
						elif ans3 == '3':
							ans4 = input("Tier 1 or 2? ")
							if ans4 == '1':
								pass
								#changeweight t1 ohp
							elif ans4 == '2':
								pass
								#changeweight t2 ohp
							else:
								print("Invalid Input")
						elif ans3 == '4':
							ans4 = input("Tier 1 or 2? ")
							if ans4 == '1':
								pass
								#changeweight t1 dl
							elif ans4 == '2':
								pass
								#changeweight t2 dl
							else:
								print("Invalid Input")
						elif ans3 == '5':
							ans4 = input("Tier 1 or 2? ")
							if ans4 == '1':
								pass
								#changeweight t1 row
							elif ans4 == '2':
								pass
								#changeweight t2 row
							else:
								print("Invalid Input")
					#Change Repranges
					elif ans2 == '2':
						self.clear()
						print("\nWhat lift's weight would you like to change?\n============================================\n0. Return to previous menu\n1. Squat\n2. Bench Press\n3. Overhead Press\n4. Deadlift\n5. Barbell Rows\n")
						ans3 = input("What would you like to do? ")
						if ans3 == '0':
							break
						elif ans3 == '1':
							ans4 = input("Tier 1 or 2? ")
							if ans4 == '1':
								pass
								#changeweight t1 squat
							elif ans4 == '2':
								pass
								#changeweight t2 squat
							else:
								print("Invalid Input")
						elif ans3 == '2':
							ans4 = input("Tier 1 or 2? ")
							if ans4 == '1':
								pass
								#changeweight t1 bench
							elif ans4 == '2':
								pass
								#changeweight t2 bench
							else:
								print("Invalid Input")
						elif ans3 == '3':
							ans4 = input("Tier 1 or 2? ")
							if ans4 == '1':
								pass
								#changeweight t1 ohp
							elif ans4 == '2':
								pass
								#changeweight t2 ohp
							else:
								print("Invalid Input")
						elif ans3 == '4':
							ans4 = input("Tier 1 or 2? ")
							if ans4 == '1':
								pass
								#changeweight t1 dl
							elif ans4 == '2':
								pass
								#changeweight t2 dl
							else:
								print("Invalid Input")
						elif ans3 == '5':
							ans4 = input("Tier 1 or 2? ")
							if ans4 == '1':
								pass
								#changeweight t1 row
							elif ans4 == '2':
								pass
								#changeweight t2 row
							else:
								print("Invalid Input")
					else:
						print("Invalid Input")


				
			else:
				print("Invalid Input")	
