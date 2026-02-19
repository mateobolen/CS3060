import pybullet as p
import math
import pybullet_data
import time
import pyrosim.pyrosim as pyrosim
import numpy
import random

pi = math.pi

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.configureDebugVisualizer(p.COV_ENABLE_GUI,0)

simulationLength = 10000

amplitude_front = pi/6
frequency_front = 40
phaseOffset_front = 0

amplitude_back = pi/2
frequency_back = 20
phaseOffset_back = pi/4

frontTargetVals = (numpy.sin(frequency_front * numpy.linspace(0, 2*pi, simulationLength) + phaseOffset_front)) * amplitude_front
backTargetVals = (numpy.sin(frequency_back * numpy.linspace(0, 2*pi, simulationLength) + phaseOffset_back)) * amplitude_back

numpy.save("data/frontTargetValues.npy", frontTargetVals)
numpy.save("data/backTargetValues.npy", backTargetVals)

p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")
backLegSensorValues = numpy.zeros(simulationLength)
frontLegSensorValues = numpy.zeros(simulationLength)
#print(backLegSensorValues)

#exit()

pyrosim.Prepare_To_Simulate(robotId)
for step in range(simulationLength):
	p.stepSimulation()
	backLegSensorValues[step] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
	frontLegSensorValues[step] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
	pyrosim.Set_Motor_For_Joint(
	bodyIndex = robotId,
	jointName = b'Torso_BackLeg',
	controlMode = p.POSITION_CONTROL,
	targetPosition = frontTargetVals[step],
	maxForce = 50)
	pyrosim.Set_Motor_For_Joint(
	bodyIndex = robotId,
	jointName = b'Torso_FrontLeg',
	controlMode = p.POSITION_CONTROL,
	targetPosition = backTargetVals[step],
	maxForce = 50)
	time.sleep(0.001)
	#print(step)
"""
step = 0
while True:
	p.stepSimulation()
	backLegTouch = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
	print(backLegTouch)
	time.sleep(0.001)
	step += 1
	#print(step)
"""

numpy.save("data/backLegSensorValues.npy", backLegSensorValues)
numpy.save("data/frontLegSensorValues.npy", frontLegSensorValues)

p.disconnect()