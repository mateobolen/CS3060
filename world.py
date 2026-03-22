import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim

class WORLD:

	def __init__(self, p):
		self.planeId = p.loadURDF("plane.urdf")
		p.loadSDF("world.sdf")