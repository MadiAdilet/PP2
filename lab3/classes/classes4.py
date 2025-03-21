import math

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def show(self):
        print(f"Координаты точки: ({self.x}, {self.y})")

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def dist(self, other_point):
        return math.sqrt((self.x - other_point.x)**2 + (self.y - other_point.y)**2)

p1 = Point(2, 3)
p2 = Point(5, 7)

p1.show()
p2.show()

distance = p1.dist(p2)
print(f"Расстояние между точками: {distance}")

p1.move(1, 1)
p1.show()