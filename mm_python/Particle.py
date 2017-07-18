import numpy as np


class Particle(object):
    """
    Class to create Particle objects. The main attributes are cartesian
    coordinates (position), velocity
    and parameters (parms). This last parameter will
    contain the force field parameters (e.g. sigma and epsilon if Lennard
    Jones potential)
    """
    def __init__(self):

        self.parms = np.empty((2, ), dtype=np.float64)