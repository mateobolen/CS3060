import pybullet as p
import time

physicsClient = p.connect(p.GUI)
for step in range(1000):
	p.stepSimulation()
	time.sleep(0.016)
	print(step)
p.disconnect()