#from .ForceField import LennardJones
#from .Simulation import Simulation
#from .ForceFieldManager import ForceFieldManager
#from .BoxManager import BoxManager, Box
import numpy as np
import mm_python as mmpy 

reducedTemperature = 0.85
reducedDensity = 0.003
numParticles = 500

sigma = 3.73
epsilon = 148.0

realTemperature = epsilon * reducedTemperature

boxLength = reducedDensity / np.power(sigma, 3)
boxLength = np.power(numParticles / boxLength, 0.333)

myBox = mmpy.Box(length=boxLength)
myBoxManager = mmpy.BoxManager(myBox)
myBoxManager.addParticles(n=numParticles, method="lattice")
#myBoxManager.getConfigFromFile(restartFile = "nistConfig.xyz")

myForceField = mmpy.ForceField.LennardJones(
    parms=(sigma, epsilon), cutoff=3 * sigma)

myForceFieldManager = mmpy.ForceFieldManager(myForceField)
myForceFieldManager.assignSystemForceField(myBox)

mySimulation = mmpy.Simulation(
    method="monteCarlo",
    temperature=realTemperature,
    steps=1000000,
    printProp=1000,
    printXYZ=1000,
    maxDisp=sigma,
    ffManager=myForceFieldManager,
    boxManager=myBoxManager)

mySimulation.run()

#mySimulation.analyze.getRDF(parms)