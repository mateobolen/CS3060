import pybullet as p
import math
import pybullet_data
import time
import pyrosim.pyrosim as pyrosim
import numpy
import random
import constants as c
from simulation import SIMULATION
# pi = c.pi

# physicsClient = p.connect(p.GUI)
# p.setAdditionalSearchPath(pybullet_data.getDataPath())
# p.configureDebugVisualizer(p.COV_ENABLE_GUI,0)

# frontTargetVals = (numpy.sin(c.frequency_front * numpy.linspace(0, 2*pi, c.simulationLength) + c.phaseOffset_front)) * c.amplitude_front
# backTargetVals = (numpy.sin(c.frequency_back * numpy.linspace(0, 2*pi, c.simulationLength) + c.phaseOffset_back)) * c.amplitude_back

# numpy.save("data/frontTargetValues.npy", frontTargetVals)
# numpy.save("data/backTargetValues.npy", backTargetVals)

# p.setGravity(0,0,-9.8)
# planeId = p.loadURDF("plane.urdf")
# robotId = p.loadURDF("body.urdf")
# p.loadSDF("world.sdf")
# backLegSensorValues = numpy.zeros(c.simulationLength)
# frontLegSensorValues = numpy.zeros(c.simulationLength)
# #print(backLegSensorValues)

# #exit()

# pyrosim.Prepare_To_Simulate(robotId)
# for step in range(c.simulationLength):
# 	p.stepSimulation()
# 	backLegSensorValues[step] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
# 	frontLegSensorValues[step] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
# 	pyrosim.Set_Motor_For_Joint(
# 	bodyIndex = robotId,
# 	jointName = b'Torso_BackLeg',
# 	controlMode = p.POSITION_CONTROL,
# 	targetPosition = frontTargetVals[step],
# 	maxForce = 50)
# 	pyrosim.Set_Motor_For_Joint(
# 	bodyIndex = robotId,
# 	jointName = b'Torso_FrontLeg',
# 	controlMode = p.POSITION_CONTROL,
# 	targetPosition = backTargetVals[step],
# 	maxForce = 50)
# 	time.sleep(0.001)
# 	#print(step)
# """
# step = 0
# while True:
# 	p.stepSimulation()
# 	backLegTouch = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
# 	print(backLegTouch)
# 	time.sleep(0.001)
# 	step += 1
# 	#print(step)
# """

# numpy.save("data/backLegSensorValues.npy", backLegSensorValues)
# numpy.save("data/frontLegSensorValues.npy", frontLegSensorValues)

# p.disconnect()

simulation = SIMULATION()
simulation.run()