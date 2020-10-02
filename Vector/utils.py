import math

from numpy.core.multiarray import ndarray


def segmentLength(a: ndarray, b: ndarray):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2 + (a[2] - b[2]) ** 2)


def innerProduct(a: ndarray, b: ndarray):
    return a @ b
