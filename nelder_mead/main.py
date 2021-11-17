from __future__ import annotations
from typing import List
from math import sqrt


class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __add__(self, other: Point):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Point):
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar: int):
        return Point(self.x * scalar, self.y * scalar)

    def __truediv__(self, scalar: int):
        return Point(self.x / scalar, self.y / scalar)

    def __str__(self):
        return f"Point({self.x}, {self.y})"


def contraction(w: Point, m: Point):
    return (w + m) / 2


def expansion(r: Point, m: Point):
    return (r * 2) - m


def shrink(b: Point, w: Point):
    return (b + w) / 2


def reflection(m: Point, w: Point):
    return (m * 2) - w


def midpoint(b: Point, g: Point):
    return (b + g) / 2


def distance(p1: Point, p2: Point):
    return sqrt(((p2.x - p1.x)**2) + ((p2.y - p1.y)**2))


def nelder_mead(f):
    v1 = Point(0, 0)
    v2 = Point(1.2, 0)
    v3 = Point(0, 0.8)

    values: List[Point] = [v1, v2, v3]
    values.sort(key=lambda point: f(point))

    B: Point = values[0]  # best
    G: Point = values[1]  # good
    W: Point = values[2]  # worst

    while distance(B, W) > 0.001:
        M: Point = midpoint(B, G)
        R: Point = reflection(M, W)

        if f(R) < f(G):  # case (i)
            if f(B) < f(R):
                W = R  # replace W with R
            else:
                # compute E and f(E)
                E: Point = expansion(R, M)
                if f(E) < f(B):
                    W = E  # replace W with E
                else:
                    W = R  # replace W with R
        else:  # case (ii)
            if f(R) < f(W):
                W = R
            C = contraction(W, M)
            if f(C) < f(W):
                W = C
            else:
                S = shrink(B, W)
                W = S
                G = M

        values: List[Point] = [B, G, W]
        values.sort(key=lambda point: f(point))
        B, G, W = values
    return B


def sphere(p: Point) -> float:
    return (p.x * p.x) + (p.y * p.y)


def ronsenbrock(p: Point):
    return (1 - p.x) + 100*((p.y-(p.x*p.x))*(p.y-(p.x*p.x)))


result = nelder_mead(ronsenbrock)
print(result)
