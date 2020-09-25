from dataclasses import dataclass

from Shape.Shape import Shape


@dataclass
class Sphere(Shape):
    radius: int
