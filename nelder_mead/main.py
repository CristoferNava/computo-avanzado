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
        return f"Point({self.x:.2f}, {self.y:.2f})"


def contraction(W: Point, M: Point) -> Point:
    return (W + M) / 2


def expansion(R: Point, M: Point) -> Point:
    return (R * 2) - M


def shrink(B: Point, W: Point) -> Point:
    return (B + W) / 2


def reflection(M: Point, W: Point) -> Point:
    return (M * 2) - W


def midpoint(B: Point, G: Point) -> Point:
    return (B + G) / 2


def distance(p1: Point, p2: Point) -> Point:
    return sqrt(((p2.x - p1.x)**2) + ((p2.y - p1.y)**2))


def nelder_mead(f):
    vertice1 = Point(0, 0)
    vertice2 = Point(1.2, 0)
    vertice3 = Point(0, 0.8)

    values: List[Point] = [vertice1, vertice2, vertice3]
    values.sort(key=lambda point: f(point))
    for value in values:
        print(value)

    B: Point = values[0]  # best
    G: Point = values[1]  # good
    W: Point = values[2]  # worst

    while distance(B, W) > 0.0001:
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


def ronsenbrock(p: Point) -> float:
    return (1 - p.x) + 100*((p.y-(p.x*p.x))*(p.y-(p.x*p.x)))


def example(p: Point) -> float:
    return p.x**2 - 4*p.x + p.y**2 - p.y - p.x*p.y


result = nelder_mead(example)
print(result)
