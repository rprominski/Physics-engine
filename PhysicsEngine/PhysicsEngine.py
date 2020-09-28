import itertools
import math
import time
from typing import List

from Body.Body import Body
from BodyMover.BodyMover import moveBody
from CollisionHandler.CollisionHandler import areColliding, elasticCollision
from DataVisualiser.DataVisualiser import drawAllBodies
from TemporaryForce.TemporaryForce import TemporaryForce
from Vector.Vector3 import Vector3


class PhysicsEngine:
    bodies: List[Body] = []
    globalResultantForce = Vector3(0, 0, 0)
    resultantGravity = Vector3(0, 0, 0)
    temporaryForces: List[TemporaryForce] = []
    tickInterval = 0.5

    def addBody(self, body: Body):
        self.bodies.append(body)

    def addGlobalForce(self, force):
        self.globalResultantForce += force

    def addGravity(self, gravity: Vector3):
        self.resultantGravity += gravity

    def moveAllBodies(self):
        resultantForce = self.globalResultantForce + self.countResultantTemporaryForce()
        for body in self.bodies:
            moveBody(body, resultantForce, self.resultantGravity, self.tickInterval)

    def addTemporaryForce(self, force: Vector3, duration: float, ticks: bool = True):
        if not ticks:
            duration = duration / self.tickInterval
        self.temporaryForces.append(TemporaryForce(force, math.ceil(duration)))

    def tick(self):
        self.temporaryForces = [x for x in self.temporaryForces if x.tickAndCheck()]
        self.checkCollisions()
        self.moveAllBodies()

    def start(self):
        while True:
            self.tick()
            drawAllBodies(self.bodies)
            time.sleep(self.tickInterval)

    def countResultantTemporaryForce(self):
        resultantForce = Vector3(0, 0, 0)

        for force in self.temporaryForces:
            resultantForce += force.force

        return resultantForce

    def checkCollisions(self):
        for pair in itertools.combinations(self.bodies, 2):
            if areColliding(pair[0], pair[1]):
                elasticCollision(pair[0], pair[1])
