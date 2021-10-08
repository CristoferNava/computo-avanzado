from __future__ import annotations


class Point:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other: Point):
        if isinstance(other, Point):
            return Point(self.x+other.x, self.y+other.y, self.x+other.x)
        elif isinstance(other, tuple):
            return Point(self.x+other[0], self.y+other[1], self.x+other[2])

    def __radd__(self, other: Point):
        if isinstance(other, Point):
            return Point(self.x+other.x, self.y+other.y, self.x+other.x)
        elif isinstance(other, tuple):
            return Point(self.x+other[0], self.y+other[1], self.x+other[2])

    def __sub__(self, other: Point):
        return Point(self.x-other.x, self.y-other.y, self.x-other.x)

    def __str__(self) -> str:
        return f'[{self.x} {self.y} {self.z}]'


p1 = Point(1, 1, 1)
p2 = Point(2, 2, 2)
p3: Point = p1 + (1, 1, 1)  # thanks to __add__
p4: Point = (1, 1, 1) + p1  # thanks to __radd__
