import constants as c
import pyrosim.pyrosim as pyrosim
import pybullet as p
import numpy


class MOTOR:
	def __init__(self, name):
		self.jointName = name
	# 	self.prepare_to_act()

	# def prepare_to_act(self):
		self.amplitude = c.amplitude_front
		self.frequency = c.frequency_front
		self.offset = c.phaseOffset_front
		self.motorValues = numpy.linspace(0, 2*c.pi, c.simulationLength)
	
	def set_value(self, robotId, i):
			pyrosim.Set_Motor_For_Joint(
			bodyIndex = robotId,
			jointName = self.jointName,
			controlMode = p.POSITION_CONTROL,
			targetPosition = self.motorValues[i],
			maxForce = 50)

			def save_values(self):
				numpu.save('data/' + self.joint_name + 'MotorTargetValues.npy', self.motorValues)