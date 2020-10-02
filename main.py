import threading
from time import sleep
from typing import List

import numpy as np

from Body.Body import Body
from Body.ImmovableBody import ImmovableBody
from DataVisualiser.DataVisualiser import startVisualistion
from PhysicsEngine.PhysicsEngine import PhysicsEngine
from Shape.Sphere import Sphere


def generateSpheresCage():
    bodies: List[Body] = []
    for i in range(20):
        body = ImmovableBody(np.array([90, -100 + i * 10 + 1, 0]), np.array([0, 0, 0]), 1.0, Sphere(5))
        body2 = ImmovableBody(np.array([-100, -100 + i * 10 + 1, 0]), np.array([0, 0, 0]), 1.0, Sphere(5))
        body3 = ImmovableBody(np.array([-100 + i * 10, -100 + 1, 0]), np.array([0, 0, 0]), 1.0, Sphere(5))
        body4 = ImmovableBody(np.array([-100 + i * 10, 100 + 1, 0]), np.array([0, 0, 0]), 1.0, Sphere(5))
        bodies.append(body)
        bodies.append(body2)
        bodies.append(body3)
        bodies.append(body4)
    return bodies


def engineThread():
    sleep(1)
    while True:
        engine = PhysicsEngine()
        engine.tickInterval = 0.01
        engine.addGravity(np.array([10, 70, 0]))
        body = Body(np.array([50, 30, 0]), np.array([100, 0, 0]), 1.0, Sphere(5))
        engine.addBody(body)
        for b in generateSpheresCage():
            engine.addBody(b)
        engine.start()


threading.Thread(target=engineThread).start()
startVisualistion()
