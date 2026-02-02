import pybullet as p
import pybullet_data
import time

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.configureDebugVisualizer(p.COV_ENABLE_GUI,0)

p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
planeId = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")

"""
for step in range(1000):
	p.stepSimulation()
	time.sleep(0.016)
	print(step)
"""

step = 0
while True:
	p.stepSimulation()
	time.sleep(0.001)
	step += 1
	#print(step)

p.disconnect()