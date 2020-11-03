import json
from json import JSONEncoder

class Lift():
	def __init__(self):

		self._name = "OHP"
		self._tier = 2
		self._sets = 5
		self._reps = 3

		_weight_progression = 5

	#def loadFile(self):
		#file = open('lifts.json', 'r')
		#self = json.load(file)
		#file.close()

	def saveFile(self):
		file = open('lifts.json', 'w')
		json.dump(self.to_json(), file)
		file.close()

	def to_json(self):
		return json.dumps(self, default=lambda o: o.__dict__) 


lift = Lift()
lift.saveFile()

