from numpy.core.multiarray import ndarray

from Body.Body import Body
from Body.ImmovableBody import ImmovableBody


def moveBody(body: Body, globalResultantforce: ndarray, resultantGravity: ndarray, time: float):
    if isinstance(body, ImmovableBody):
        return

    acceleration = globalResultantforce * body.mass + resultantGravity
    body.setPosition(body.position + body.velocity * time + (acceleration * time ** 2) / 2)
    body.setVelocity(body.velocity + acceleration * time)
