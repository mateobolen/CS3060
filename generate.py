import pyrosim.pyrosim as pyrosim



def Create_World():
	pyrosim.Start_SDF("world.sdf")
	length = 1
	width = 1
	height = 1
	pyrosim.Send_Cube(name="Box", pos=[3,3,0.5] , size=[length,width,height])
	pyrosim.End()

def Generate_body():
	pyrosim.Start_URDF("body.urdf")
	pyrosim.Send_Cube(name="Torso", pos=[0,0,1.5] , size=[1,1,1])
	pyrosim.Send_Joint( name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = [-0.5,0,1])
	pyrosim.Send_Cube(name="BackLeg", pos=[-0.5,0,-0.5] , size=[1,1,1])
	pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = [0.5,0,1])
	pyrosim.Send_Cube(name="FrontLeg", pos=[0.5,0,-0.5] , size=[1,1,1])
	pyrosim.End()

def Generate_brain():
	pyrosim.Start_NeuralNetwork("brain.nndf")
	pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
	pyrosim.Send_Sensor_Neuron(name = 1, linkName = "BackLeg")
	pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "FrontLeg")
	pyrosim.End()




if __name__ == '__main__':
	Create_World()
	print("Generated world")

	Generate_body()
	print("Created robot")

	Generate_brain()
	print("Created brain")