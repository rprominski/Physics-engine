from Shape.Shape import Shape
from Vector.Vector3 import Vector3


class Body:
    position: Vector3
    velocity: Vector3
    shape: Shape
    mass: float

    def __init__(self, positon: Vector3, velocity: Vector3, mass: float, shape: Shape):
        self.position = positon
        self.velocity = velocity
        self.mass = mass
        self.shape = shape

    def setPosition(self, position):
        self.position = position

    def setVelocity(self, velocity):
        self.velocity = velocity
