from Body.Body import Body

from Body.ImmovableBody import ImmovableBody
from Vector.Vector3 import Vector3


def moveBody(body: Body, globalResultantforce: Vector3, resultantGravity: Vector3, time: float):
    if isinstance(body, ImmovableBody):
        return

    acceleration = globalResultantforce * body.mass + resultantGravity
    body.setPosition(body.position + body.velocity * time + (acceleration * time ** 2) / 2)
    body.setVelocity(body.velocity + acceleration * time)
