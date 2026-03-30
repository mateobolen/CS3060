import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import time
from world import WORLD
from robot import ROBOT
import constants as c

class SIMULATION:

	def __init__(self):
		self.physicsClient = p.connect(p.GUI)
		p.setAdditionalSearchPath(pybullet_data.getDataPath())
		p.configureDebugVisualizer(p.COV_ENABLE_GUI,0)
		p.setGravity(0,0,-9.8)
		self.world = WORLD(p)
		self.robot = ROBOT(p)


	def __del__(self):
		p.disconnect()
		print('destruction')
		
	def run(self):
		for step in range(c.simulationLength):
			print(step)
			p.stepSimulation()
			self.robot.sense(step)
			self.robot.act(step)
			time.sleep(0.001)

	def generateTargetValues(self):
		frontTargetVals = (numpy.sin(c.frequency_front * numpy.linspace(0, 2*pi, c.simulationLength) + c.phaseOffset_front)) * c.amplitude_front
		backTargetVals = (numpy.sin(c.frequency_back * numpy.linspace(0, 2*pi, c.simulationLength) + c.phaseOffset_back)) * c.amplitude_back



		

