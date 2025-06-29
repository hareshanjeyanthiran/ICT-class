
class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"



class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def __str__(self):
        return f"Square(side={self.width})"



rect = Rectangle(4, 6)
print(rect)
print("Area:", rect.area())
print("Perimeter:", rect.perimeter())

square = Square(5)
print(square)
print("Area:", square.area())
print("Perimeter:", square.perimeter())