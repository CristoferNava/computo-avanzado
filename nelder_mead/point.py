from __future__ import annotations


class Point:
    "A simple 2D point"

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
