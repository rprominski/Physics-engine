from typing import List

from Body.Body import Body


def printConsole(bodies: List[Body]):
    for i in range(len(bodies)):
        print(f"body nr {i}, position: {bodies[i].position}")
    print()
