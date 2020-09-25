from dataclasses import dataclass


@dataclass
class Vector3:
    x: float
    y: float
    z: float

    def __init__(self, x: float, y: float, z: float):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other: 'Vector3'):
        return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __radd__(self, other: 'Vector3'):
        return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other: 'Vector3'):
        return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other: float):
        return Vector3(self.x * other, self.y * other, self.z * other)

    def __rmul__(self, other: float):
        return Vector3(self.x * other, self.y * other, self.z * other)

    def __truediv__(self, other: float):
        return Vector3(self.x / other, self.y / other, self.z / other)
