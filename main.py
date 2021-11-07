class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def get_area(self):
        return self.height * self.width

    def __gt__(self, other):
        if not isinstance(other, Rectangle):
            return NotImplemented
        return Rectangle.get_area(self) > other.get_area()

    def __lt__(self, other):
        if not isinstance(other, Rectangle):
            return NotImplemented
        return Rectangle.get_area(self) < other.get_area()

    def __add__(self, other):
        if not isinstance(other, Rectangle):
            return NotImplemented
        return Rectangle.get_area(self) + other.get_area()

    def __mul__(self, other):
        if not isinstance(other, int or float):
            return NotImplemented
        return Rectangle.get_area(self) * other


rec1 = Rectangle(7, 2)
rec2 = Rectangle(8, 4)

print(Rectangle.__gt__(rec1, rec2))
print(Rectangle.__lt__(rec1, rec2))
print(Rectangle.__add__(rec1, rec2))
print(Rectangle.__mul__(rec1, 8))
