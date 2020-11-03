import json

def filewrite(input):
	with open('data.json','w') as file:
		json.dump(input,file)

def fileread():
	with open('data.json','r') as file:
		data = json.load(file)
	return data
	#optimize program to use this function
def settingsMenu():
	with open('data.json','r') as file:
		data = json.load(file)

	rin = 0
	while rin == 0:
		print("""
\n0.Go back to main menu
1.Change an exercise weight
2.Change an exercise reprange
3.Change bar weight""")
		ans = input("\nWhat would you like to do? ")
		ans = int(ans)
		if ans == 0:
			rin = 1
		elif ans == 1:
			rin2 = 0
			while rin2 == 0:
				print("""
					\n
0.Go back to settings menu
1. Tier 1 Squat
2. Tier 1 Bench Press
3. Tier 1 Overhead Press
4. Tier 1 Deadlift
5. Tier 2 Squat
6. Tier 2 Bench Press
7. Tier 2 Overhead Press
8. Tier 2 Deadlift
					""")
				ans2 = input("\nWhat exercise weight would you like to change?")
				ans2 = int(ans2)
				if ans2 == 0:
					rin2 = 99
				elif ans2 == 1:
					modifyWeight("t1sq")
				elif ans2 == 2:
					modifyWeight("t1bp")
				elif ans2 == 3:
					modifyWeight("t1ohp")
				elif ans2 == 4:
					modifyWeight("t1dl")
				elif ans2 == 5:
					modifyWeight("t2sq")
				elif ans2 == 6:
					modifyWeight("t2bp")
				elif ans2 == 7:
					modifyWeight("t2ohp")
				elif ans2 == 8:
					modifyWeight("t2dl")
				print("\n-------------------------------------------------------------")
		elif ans == 2:
			print("yippee")
		elif ans == 3:
			ans2 = input(f"The current current bar weight is {data['bar']}. What would you like to change it to? ")
			data['bar'] = int(ans2)
			print("\n-------------------------------------------------------------")
			filewrite(data)
		else:
			print("Invalid input")

def modifyWeight(exercise):
	with open('data.json','r') as file:
		data = json.load(file)
	newWeight = input(f"Current weight for that exercise is {data['weights'][exercise]}. What would you like to change it to?")
	data['weights'][exercise] = int(newWeight)
	filewrite(data)

def workout(t1, t2):
	with open('data.json','r') as file:
		data = json.load(file)

	t1reps = data['reprange'][t1]['reps']
	t1sets = data['reprange'][t1]['sets']
	t1weight = data['weights'][t1]
	t2reps = data['reprange'][t2]['reps']
	t2sets = data['reprange'][t2]['sets']
	t2weight = data['weights'][t2]
	rin = 1
	t1name = label_exercise(t1)
	t2name = label_exercise(t2)
	#tier 1 exercise
	print(f"\nWorkout Day 1: Tier 1 {t1name}! Do {t1sets} sets of {t1reps} reps at {t1weight} lbs.")
	while rin <= t1sets:
		inp = input(f'\nWere you able to finish set {rin}? (Y/N)  ') 
		if rin == t1sets and inp.lower() == 'y':
			if t1name == 'Overhead Press' or t1name == 'Bench Press':
				data['weights'][t1] = t1weight + 5
			else:
				data['weights'][t1] = t1weight + 10
			t1weight = data['weights'][t1]
			print(f'\nGreat Job! Next time you do this exercise you\'ll do {t1sets} sets of {t1reps} reps at {t1weight} lbs. \n-------------------------------------------------------------')
			filewrite(data)
		rin += 1
		if inp.lower() == 'n':
			inp = input('\nDon\'t sweat it! Would you like to adjust your rep-range? (Y/N) ')
			if inp.lower() == 'y': #Make cases for deadlift and send to t2 workout as well
				if t1sets == 5:
					data['reprange'][t1]['sets'] = 6
					data['reprange'][t1]['reps'] = 2
					t1reps = data['reprange'][t1]['reps']
					t1sets = data['reprange'][t1]['sets']
					filewrite(data)
					print(f'\nThat\'s fine! Next time you do this exercise you\'ll do {t1sets} sets of {t1reps} reps at {t1weight} lbs.\n-------------------------------------------------------------')
					break
				elif t1sets == 6:
					data['reprange'][t1]['sets'] = 10
					data['reprange'][t1]['reps'] = 1
					t1reps = data['reprange'][t1]['reps']
					t1sets = data['reprange'][t1]['sets']
					filewrite(data)
					print(f'\nDon\'t sweat it! Next time you do this exercise you\'ll do {t1sets} sets of {t1reps} reps at {t1weight} lbs.\n-------------------------------------------------------------')
					break
				else:
					data['reprange'][t1]['sets'] = 5
					data['reprange'][t1]['reps'] = 3
					newWeight = input(f'\nWhat would you like your new working weight to be? Your current weight is {t1weight}: ')
					newWeight = int(newWeight)
					data['weights'][t1] = newWeight
					filewrite(data)
					t1reps = data['reprange'][t1]['reps']
					t1sets = data['reprange'][t1]['sets']
					t1weight = data['weights'][t1]
					print(f'\nNext time you do this exercise you\'ll do {t1sets} sets of {t1reps} reps at {t1weight} lbs.\n-------------------------------------------------------------')
					break
			else: 
				rin = 99
				break
	#tier 2 exercise 
	rin = 1
	print(f"\nWorkout Day 1: Tier 2 {t2name}! Do {t2sets} sets of {t2reps} reps at {t2weight} lbs.")
	while rin <= t2sets: 
		inp = input(f'\nWere you able to finish set {rin}? (Y/N)  ') 
		if rin == t2sets and inp.lower() == 'y':
			data['weights'][t2] = t2weight + 5
			t2weight = data['weights'][t2]
			print(f'\nGreat Job! Next time you do this exercise you\'ll do {t2sets} sets of {t2reps} reps at {t2weight} lbs.\n-------------------------------------------------------------')
			filewrite(data)
		rin += 1
		if inp.lower() == 'n': #copy case for deadlift
			inp = input('\nDon\'t sweat it! Would you like to adjust your rep-range? (Y/N) ')
			if inp.lower() == 'y':
				if t2reps == 10:
					data['reprange'][t2]['reps'] = 8
					t2reps = data['reprange'][t2]['reps']
					t2sets = data['reprange'][t2]['sets']
					filewrite(data)
					print(f'\nNo problem! Next time you do this exercise you\'ll do {t2sets} sets of {t2reps} reps at {t2weight} lbs.\n-------------------------------------------------------------')
					break
				elif t2reps == 8:
					data['reprange'][t2]['reps'] = 6
					t2reps = data['reprange'][t2]['reps']
					t2sets = data['reprange'][t2]['sets']
					filewrite(data)
					print(f'\nNo problem! Next time you do this exercise you\'ll do {t2sets} sets of {t2reps} reps at {t2weight} lbs.\n-------------------------------------------------------------')
					break
				else:
					data['reprange'][t2]['reps'] = 10
					newWeight = input(f'\nWhat would you like your new working weight to be? Your current weight is {t2weight}: ')
					newWeight = int(newWeight)
					data['weights'][t2] = newWeight
					filewrite(data)
					t1reps = data['reprange'][t1]['reps']
					t1sets = data['reprange'][t1]['sets']
					t1weight = data['weights'][t1]
					print(f'\nNext time you do this exercise you\'ll do {t2sets} sets of {t2reps} reps at {t2weight} lbs.\n-------------------------------------------------------------')
					break
			else:
				rin = 99
				break
	rin += 1 


def label_exercise(lift):
	if 'sq' in lift:
		return 'Squat'
	elif 'ohp' in lift:
		return 'Overhead Press'
	elif 'dl' in lift: 
		return 'Deadlift'
	elif 'bp' in lift:
		return 'Bench Press'

#base lifts
bar = 25
weights = {
	"t1sq":200,
	"t1ohp":100,
	"t1dl":250,
	"t1bp":150,
	"t2sq":150,
	"t2ohp":75,
	"t2dl":200,
	"t2bp":125
}
reprange = {
	"t1sq":{'sets':5, 'reps':3},
	"t1ohp":{'sets':5, 'reps':3},
	"t1dl":{'sets':5, 'reps':3},
	"t1bp":{'sets':5, 'reps':3},
	"t2sq":{'sets':3, 'reps':10},
	"t2ohp":{'sets':3, 'reps':10},
	"t2dl":{'sets':3, 'reps':10},
	"t2bp":{'sets':3, 'reps':10}
}
baselifts = {"weights":weights,"reprange":reprange, "bar":bar}
#filewrite(baselifts) #
#uncomment to reset progress

#Menu
rin = 0
while rin == 0:
	print("\n-------------------------------------------------------------")
	print("""
Welcome to GZCLP tracker!
0. Close Program
1. Start Workout Day 1 (Tier 1 Squat, Tier 2 Bench Press)
2. Start Workout Day 2 (Tier 1 Overhead Press, Tier 2 Deadlift)
3. Start Workout Day 3 (Tier 1 Bench Press, Tier 2 Squat)
4. Start Workout Day 4 (Tier 1 Deadlift, Tier 2 Overhead Press)
5. Print Lifts
6. Settings
		""")
	ans = input("What would you like to do? ")
	if ans=='0':
		rin = 1
	elif ans=='1':
		workout('t1sq', 't2bp')
	elif ans=='2':
		workout('t1ohp', 't2dl')
	elif ans=='3':
		workout('t1bp', 't2sq')
	elif ans=='4':
		workout('t1dl', 't2ohp')
	elif ans=='5':
		data = fileread()
		print(f"\nTier 1 Squat {data['weights']['t1sq']} lbs reprange {data['reprange']['t1sq']['sets']}x{data['reprange']['t1sq']['reps']}")
		print(f"Tier 1 Overhead Press {data['weights']['t1ohp']} lbs rep range {data['reprange']['t1ohp']['sets']}x{data['reprange']['t1ohp']['reps']}")
		print(f"Tier 1 Bench Press {data['weights']['t1bp']} lbs rep range {data['reprange']['t1bp']['sets']}x{data['reprange']['t1bp']['reps']}")
		print(f"Tier 1 Deadlift {data['weights']['t1dl']} lbs reprange {data['reprange']['t1dl']['sets']}x{data['reprange']['t1dl']['reps']}")
		print(f"\nTier 2 Squat {data['weights']['t2sq']} lbs reprange {data['reprange']['t2sq']['sets']}x{data['reprange']['t2sq']['reps']}")
		print(f"Tier 2 Overhead Press {data['weights']['t2ohp']} lbs reprange {data['reprange']['t2ohp']['sets']}x{data['reprange']['t2ohp']['reps']}")
		print(f"Tier 2 Bench Press {data['weights']['t2bp']} lbs reprange {data['reprange']['t2bp']['sets']}x{data['reprange']['t2bp']['reps']}")
		print(f"Tier 2 Deadlifts {data['weights']['t2dl']} lbs reprange {data['reprange']['t2dl']['sets']}x{data['reprange']['t2dl']['reps']}")
	elif ans=='6':
		settingsMenu()
	else:
		print("Invalid Input")




