from dataclasses import dataclass

from Vector.Vector3 import Vector3


@dataclass
class TemporaryForce:
    force: Vector3
    ttl: int

    def tickAndCheck(self):
        self.ttl -= 1
        return self.ttl >= 0
