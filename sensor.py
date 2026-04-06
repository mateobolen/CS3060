import numpy
import constants as c
import pyrosim.pyrosim as pyrosim

class SENSOR:
	def __init__(self, name):
		self.linkName = name
		self.values = numpy.zeros(c.simulationLength)

	def get_value(self, t):
		self.values[t] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
		# if t == c.simulationLength - 1:
		# 	print(self.values)		