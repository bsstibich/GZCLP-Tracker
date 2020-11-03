from liftClass import Lift
import pickle

sq1 = Lift("Squat", 1, 5, 3, 305, 10)
bp1 = Lift("Bench Press", 1, 5, 3, 215, 5)
ohp1 = Lift("Overhead Press", 1, 5, 3, 125, 5)
dl1 = Lift("Deadlift", 1, 5, 3, 395, 10)
row1 = Lift("Row", 1, 5, 3, 215, 5) 

baselifts = [sq1, bp1, ohp1, dl1, row1]

with open('lifts.swole', 'wb') as file: #save
	pickle.dump(baselifts, file)

#with open('lifts.swole', 'rb') as file: #load
	#lift = pickle.load(file)

#print(lift[1]._name)