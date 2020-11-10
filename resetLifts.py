from liftClass import Lift
import pickle

sq1 = Lift("Squat", 1, 5, 3, 315, 10)
bp1 = Lift("Bench Press", 1, 5, 3, 215, 5)
ohp1 = Lift("Overhead Press", 1, 5, 3, 125, 5)
dl1 = Lift("Deadlift", 1, 5, 3, 395, 10)
row1 = Lift("Row", 1, 5, 3, 215, 5) 

sq2 = Lift("Squat", 2, 3, 10, 215, 10)
bp2 = Lift("Bench Press", 2, 3, 10, 150, 5)
ohp2 = Lift("Overhead Press", 3, 3, 10, 100, 5)
dl2 = Lift("Deadlift", 2, 3, 10, 250, 10)
row2 = Lift("Row", 2, 3, 10, 150, 5)


lifts = {'1': {'Squat': sq1,'Bench Press': bp1,'Overhead Press': ohp1,'Deadlift': dl1,'Row': row1}, '2':{'Squat': sq2,'Bench Press': bp2,'Overhead Press': ohp2,'Deadlift': dl2,'Row': row2}}

with open('lifts.swole', 'wb') as file: #save
	pickle.dump(lifts, file)
print("Lifts Reset.")
#with open('lifts.swole', 'rb') as file: #load
	#lift = pickle.load(file)

