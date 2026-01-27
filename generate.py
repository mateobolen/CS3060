import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("boxes.sdf")

length = 1
width = 1
height = 1


for i in range(5):
	for j in range(5):
		for k in range(10):
			pyrosim.Send_Cube(name="Box", pos=[i,j,0.5 + k] , size=[length,width,height])
			length *= 0.9
			width *= 0.9
			height *= 0.9
		length = 1
		width = 1
		height = 1

pyrosim.End()