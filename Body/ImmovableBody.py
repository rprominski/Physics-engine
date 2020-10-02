import math

import numpy as np

from Body.Body import Body


class ImmovableBody(Body):
    @property
    def mass(self):
        return math.inf

    @property
    def velocity(self):
        return np.array([0, 0, 0]);

    @velocity.setter
    def velocity(self, velocity):
        pass

    @mass.setter
    def mass(self, mass):
        pass
