from Body.Body import Body
from Body.ImmovableBody import ImmovableBody
from Shape.Sphere import Sphere
from Vector.utils import segmentLength, innerProduct


def areSpheresColliding(b, b2):
    r1 = b.shape.radius
    r2 = b2.shape.radius
    if segmentLength(b.position, b2.position) <= (r1 + r2):
        return True
    return False


def areColliding(b: Body, b2: Body):
    if isinstance(b.shape, Sphere) and isinstance(b2.shape, Sphere):
        return areSpheresColliding(b, b2)


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
