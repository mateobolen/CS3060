import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
from sensor import SENSOR
from motor import MOTOR
from pyrosim.neuralNetwork import NEURAL_NETWORK

class ROBOT:

	def __init__(self, p):
		self.robotId = p.loadURDF("body.urdf")
		pyrosim.Prepare_To_Simulate(self.robotId)
		self.prepare_to_sense()
		self.prepare_to_act()
		self.nn = NEURAL_NETWORK("brain.nndf")

	#def prepare_to_simulate(self):
		#idk

	def prepare_to_sense(self):
		self.sensors = {}
		for linkName in pyrosim.linkNamesToIndices:
			self.sensors[linkName] = SENSOR(linkName)

	def prepare_to_act(self):
		self.motors = {}
		for jointName in pyrosim.jointNamesToIndices:
			self.motors[jointName] = MOTOR(jointName) 

	def sense(self, t):
		for sensor in self.sensors.values():
			sensor.get_value(t)

	def act(self, i):
		for motor in self.motors.values():
			motor.set_value(self.robotId, i)

	def think(self):
		self.nn.Update()
		self.nn.Print()