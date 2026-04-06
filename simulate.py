import pybullet as p
import math
import pybullet_data
import time
import pyrosim.pyrosim as pyrosim
import numpy
import random
import constants as c
from simulation import SIMULATION

if __name__ == '__main__':
	simulation = SIMULATION()
	simulation.run()