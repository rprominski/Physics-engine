from dataclasses import dataclass

from numpy.core.multiarray import ndarray


@dataclass
class TemporaryForce:
    force: ndarray
    ttl: int

    def tickAndCheck(self):
        self.ttl -= 1
        return self.ttl >= 0
