import json

class Lift():
	def __init__(self):
		self._name = ""
		self._tier = 2
		self._sets = 5
		self._reps = 3

		_weight_progression = 5

	def loadFile(self):
		file = open('lifts.json', 'rb')
		self = json.load(file)
		file.close()

	def saveFile(self):
		file = open('lifts.json', 'wb')
		json.dump(self, file)
		file.close()

lift = Lift()
#lift.saveFile()
lift.loadFile()
print(lift._name)