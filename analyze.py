import numpy
import matplotlib.pyplot as matplot

backLegSensorValues = numpy.load("data/backLegSensorValues.npy")
frontLegSensorValues = numpy.load("data/frontLegSensorValues.npy")
targetVals_front = numpy.load("data/frontTargetValues.npy")
targetVals_back = numpy.load("data/backTargetValues.npy")

matplot.plot(backLegSensorValues, label='Back leg touch', linewidth=4)
matplot.plot(frontLegSensorValues, label='Front leg touch')
matplot.plot(targetVals_front, label='front leg target values')
matplot.plot(targetVals_back, label='back leg target values')
matplot.legend()
matplot.show()
