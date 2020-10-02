from numpy.core.multiarray import ndarray

from Shape.Shape import Shape


class Body:
    position: ndarray
    velocity: ndarray
    shape: Shape
    mass: float

    def __init__(self, positon: ndarray, velocity: ndarray, mass: float, shape: Shape):
        self.position = positon
        self.velocity = velocity
        self.mass = mass
        self.shape = shape

    def setPosition(self, position):
        self.position = position

    def setVelocity(self, velocity):
        self.velocity = velocity
