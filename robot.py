import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
from sensor import SENSOR

class ROBOT:

	def __init__(self, p):
		self.motors = {}

		self.robotId = p.loadURDF("body.urdf")
		pyrosim.Prepare_To_Simulate(self.robotId)
		self.prepare_to_sense()

	#def prepare_to_simulate(self):
		#idk

	def prepare_to_sense(self):
		self.sensors = {}
		for linkName in pyrosim.linkNamesToIndices:
			self.sensors[linkName] = SENSOR(linkName)

	def sense(self, t):
			for i in self.sensors:
				self.sensors[i].get_value(t)
