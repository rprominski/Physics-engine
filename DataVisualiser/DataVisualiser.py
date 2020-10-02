from typing import List

from easygraphics import *

from Body.Body import Body
from Shape.Sphere import Sphere

width: int = 800
height: int = 600
middleWidth = width / 2
middleHeight = height / 2


def printConsole(bodies: List[Body]):
    for i in range(len(bodies)):
        print(f"body nr {i}, position: {bodies[i].position}")
    print()


def getMiddlePoint():
    return width / 2, height / 2


def initGraphics():
    init_graph(width, height)
    set_render_mode(RenderMode.RENDER_MANUAL)
    set_color(Color.BLUE)
    set_fill_color(Color.RED)


def endVisualisation():
    close_graph()


def startVisualistion():
    easy_run(initGraphics)


def drawSphere(x: float, y: float, radius: float):
    draw_circle(middleWidth + x, middleHeight + y, radius)


def drawBody(body: Body):
    if isinstance(body.shape, Sphere):
        shape: Sphere = body.shape
        drawSphere(body.position[0], body.position[1], shape.radius)


def drawAllBodies(bodies: List[Body]):
    clear_device()
    for body in bodies:
        drawBody(body)
    delay(0)
