import math

from Body.Body import Body
from Vector.Vector3 import Vector3


class ImmovableBody(Body):
    @property
    def mass(self):
        return math.inf

    @property
    def velocity(self):
        return Vector3(0, 0, 0);

    @velocity.setter
    def velocity(self, velocity):
        pass

    @mass.setter
    def mass(self, mass):
        pass
