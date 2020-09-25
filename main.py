from Body.Body import Body
from Body.ImmovableBody import ImmovableBody
from PhysicsEngine.PhysicsEngine import PhysicsEngine
from Shape.Sphere import Sphere
from Vector.Vector3 import Vector3

engine = PhysicsEngine()
body = Body(Vector3(-7, 0, 0), Vector3(1, 0, 0), 1.0, Sphere(5))
body2 = ImmovableBody(Vector3(5, 1, 0), Vector3(0, 0, 0), 1.0, Sphere(5))

engine.addGravity(Vector3(1, 0, 0))
engine.addBody(body)
engine.addBody(body2)

engine.start()
