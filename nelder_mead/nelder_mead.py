import numpy as np
from typing import List
from math import sqrt
from point import Point


def contraction(W: Point, M: Point, gamma: int) -> Point:
    return ((W + M) / 2) * gamma


def expansion(R: Point, M: Point, rho: int) -> Point:
    return ((R * 2) - M) * rho


def shrink(B: Point, W: Point, sigma: int) -> Point:
    return ((B + W) / 2) * sigma


def reflection(M: Point, W: Point, alpha: int) -> Point:
    return ((M * 2) - W) * alpha


def midpoint(B: Point, G: Point) -> Point:
    return (B + G) / 2


def distance(p1: Point, p2: Point) -> Point:
    return sqrt(((p2.x - p1.x)**2) + ((p2.y - p1.y)**2))


def nelder_mead(f, alpha=1, rho=1, gamma=1, sigma=1) -> Point:
    vertice1 = Point(0, 0)
    vertice2 = Point(1.2, 0)
    vertice3 = Point(0, 0.8)

    values = np.array([vertice1.np(), vertice2.np(), vertice3.np()])
    values = values[values[:, 0].argsort()]

    B: Point = Point.np_to_point(values[0])  # best
    G: Point = Point.np_to_point(values[1])  # good
    W: Point = Point.np_to_point(values[2])  # worst

    while distance(B, W) > 0.001:
        M: Point = midpoint(B, G)
        R: Point = reflection(M, W, alpha)

        if f(R) < f(G):  # case (i)
            if f(B) < f(R):
                W = R  # replace W with R
            else:
                # compute E and f(E)
                E: Point = expansion(R, M, rho)
                if f(E) < f(B):
                    W = E  # replace W with E
                else:
                    W = R  # replace W with R
        else:  # case (ii)
            if f(R) < f(W):
                W = R
            C = contraction(W, M, gamma)
            if f(C) < f(W):
                W = C
            else:
                S = shrink(B, W, sigma)
                W = S
                G = M

        values: List[Point] = [B, G, W]
        values.sort(key=lambda point: f(point))
        B, G, W = values

    return B
