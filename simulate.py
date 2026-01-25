import pybullet as p
import time

physicsClient = p.connect(p.GUI)
#p.configureDebugVisualizer(p.COV_ENABLE_GUI,0)

p.loadSDF("box.sdf")

"""
for step in range(1000):
	p.stepSimulation()
	time.sleep(0.016)
	print(step)
"""

step = 0
while True:
	p.stepSimulation()
	time.sleep(0.016)
	step += 1
	print(step)

p.disconnect()