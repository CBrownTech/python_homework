# Task 5: Extending a Class

import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f"Point({self.x}, {self.y})"

    def __repr__(self):
        return str(self)

    def distance_to(self, other):
        if not isinstance(other, Point):
            raise TypeError("distance_to expects a Point")
        return math.dist((self.x, self.y), (other.x, other.y))


class Vector(Point):
    def __str__(self):
        return f"Vector<{self.x}, {self.y}>"

    def __repr__(self):
        return str(self)

    def __add__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return Vector(self.x + other.x, self.y + other.y)


if __name__ == "__main__":
    p1 = Point(0, 0)
    p2 = Point(3, 4)
    p3 = Point(3, 4)

    print("Points:")
    print(p1)
    print(p2)
    print(f"p2 == p3? {p2 == p3}")
    print(f"distance p1->p2: {p1.distance_to(p2)}")

    v1 = Vector(1, 2)
    v2 = Vector(3, 5)
    v3 = v1 + v2

    print("\nVectors:")
    print(v1)
    print(v2)
    print(f"v1 + v2 = {v3}")

    print("\nMixed addition (Vector + Point):")
    print(f"v1 + p2 = {v1 + p2}")