from numpy.core.multiarray import ndarray

from Vector.utils import segmentLength


def squareCircleIntersection(s: ndarray, c: ndarray, sideLength: float, radius: float):
    length = segmentLength(s, c)
