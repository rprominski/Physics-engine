from numpy.core.multiarray import ndarray

from Body.Body import Body
from Body.ImmovableBody import ImmovableBody
from Shape.Sphere import Sphere
from Vector.utils import segmentLength, innerProduct


def areSpheresIntersecting(position: ndarray, position2: ndarray, radius: float, radius2: float):
    if segmentLength(position, position2) <= (radius + radius2):
        return True
    return False


def areCubeAndSphereIntersecting(cubePosition: ndarray, spherePosition: ndarray, sideLength: float, radius):
    pass


def areColliding(b: Body, b2: Body):
    if isinstance(b.shape, Sphere) and isinstance(b2.shape, Sphere):
        s: Sphere = b.shape
        s2: Sphere = b2.shape
        return areSpheresIntersecting(b.position, b2.position, s.radius, s2.radius)


def elasticCollision(b: Body, b2: Body):
    if isinstance(b, ImmovableBody) and isinstance(b2, ImmovableBody):
        return
    if isinstance(b, ImmovableBody):
        b2.setVelocity(b2.velocity - 2 * innerProduct(b2.velocity - b.velocity,
                                                      b2.position - b.position) / segmentLength(
            b2.position, b.position) ** 2 * (b2.position - b.position))
        return
    if isinstance(b2, ImmovableBody):
        b.setVelocity(b.velocity - 2 * innerProduct(b.velocity - b2.velocity,
                                                    b.position - b2.position) / segmentLength(
            b.position, b2.position) ** 2 * (b.position - b2.position))
        return

    v = b.velocity - 2 * b2.mass / (b.mass + b2.mass) * innerProduct(b.velocity - b2.velocity,
                                                                     b.position - b2.position) / segmentLength(
        b.position, b2.position) ** 2 * (b.position - b2.position)
    v2 = b2.velocity - 2 * b.mass / (b.mass + b2.mass) * innerProduct(b2.velocity - b.velocity,
                                                                      b2.position - b.position) / segmentLength(
        b2.position, b.position) ** 2 * (b2.position - b.position)
    b.setVelocity(v)
    b2.setVelocity(v2)
