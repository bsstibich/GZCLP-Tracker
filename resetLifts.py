from liftClass import Lift
import pickle

sq1 = Lift("Squat", 1, 5, 3, 305, 10)
bp1 = Lift("Bench Press", 1, 5, 3, 215, 5)
ohp1 = Lift("Overhead Press", 1, 5, 3, 125, 5)
dl1 = Lift("Deadlift", 1, 5, 3, 395, 10)
row1 = Lift("Row", 1, 5, 3, 215, 5) 

sq2 = Lift("Squat", 2, 3, 10, 215, 10)
bp2 = Lift("Bench Press", 2, 3, 10, 150, 5)
ohp2 = Lift("Overhead Press", 3, 10, 3, 100, 5)
dl2 = Lift("Deadlift", 2, 3, 10, 250, 10)
row2 = Lift("Row", 2, 3, 10, 150, 5)


lifts = {'t1': {'sq': sq1,'bp': bp1,'ohp': ohp1,'dl': dl1,'row': row1}, 't2':{'sq': sq2,'bp': bp2,'ohp': ohp2,'dl': dl2,'row': row2}}

with open('lifts.swole', 'wb') as file: #save
	pickle.dump(lifts, file)

#with open('lifts.swole', 'rb') as file: #load
	#lift = pickle.load(file)

