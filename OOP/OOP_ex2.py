class Shape:
    def what_am_i(self):
        return print("I am Shape")

class Rectangle(Shape):
    def __init__(self, len, wight):
        self.len = len
        self.wight = wight

    def calculate_perimeter(self):
        return self.len * 2 + self.wight * 2


class Square(Shape):
    all_s = []

    def __init__(self, side):
        self.side = side
        self.all_s.append(self.side)

    def calculate_perimeter(self):
        return self.side * 4

    def change_size(self, size):
        self.side += size
        self.all_s.append(self.side)

    def __repr__(self):
        return (str(self.side) + " ")* 4


my_rectaingle = Rectangle(10, 20)
print(my_rectaingle.calculate_perimeter())
my_square = Square(10)
print(my_square.calculate_perimeter())
my_square.change_size(10)
print(my_square.calculate_perimeter())

my_square.what_am_i()
my_rectaingle.what_am_i()


class Horse:
    def __init__(self, name, number, owner):
        self.name = name
        self.number = number
        self.owner = owner


class Rider:
    def __init__(self, name):
        self.name = name


alex = Rider("Alexander Macedonian")
kon = Horse("Butcefal", 1, alex)
print(alex.name)
print(kon.owner.name)
my_square2 = Square(30)
my_square4 = Square(50)

print(Square.all_s)

print(my_square2)


def equal_or_not(x, y):
    return x is y


print(equal_or_not(1, 2))
print(equal_or_not("a", "a"))
print(equal_or_not(my_square2, my_square4))

