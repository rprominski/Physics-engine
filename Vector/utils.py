import math

from Vector.Vector3 import Vector3


def segmentLength(a: Vector3, b: Vector3):
    return math.sqrt((a.x - b.x) ** 2 + (a.y - b.y) ** 2 + (a.z - b.z) ** 2)


def innerProduct(a: Vector3, b: Vector3):
    return a.x * b.x + a.y * b.y + a.z * b.z
