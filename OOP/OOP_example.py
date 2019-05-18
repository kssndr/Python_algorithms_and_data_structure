import math


class Apple:
    def __init__(self, w, d, c, s):
        self.wight = w
        self.diameter = d
        self. color = c
        self.sort = s
        print("Apple")


a = Apple(10, 1, 'red', 'antonovka')


class Circle:
    def __init__(self, d):
        self.diameter = d

    def area(self):
        return int(self.diameter / 2 * math.pi ** 2)


my_circle = Circle(10)
print(my_circle.area())
my_circle1 = Circle(7)
print(my_circle1.area())


class Triangle:
    def __init__(self, c1, c2):
        self.catet1 = c1
        self.catet2 = c2

    def area(self):
        return (self.catet1 * self.catet2) / 2


my_triangle = Triangle(2, 4)
print(my_triangle.area())


class Hexagon:
    def __init__(self, s):
        self.side = s

    def calculate_perimeter(self):
        return self.side * 6


my_hexagon = Hexagon(5)
print(my_hexagon.calculate_perimeter())
