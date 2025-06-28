class Rectangle():
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)
class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)

    def area(self):
        return self.width * self.height
    def perimeter(self):
        return 4 * self.width

if __name__ == "__main__":
    rect = Rectangle(5, 10)
    print(f"Rectangle Area: {rect.area()}")
    print(f"Rectangle Perimeter: {rect.perimeter()}")

    square = Square(4)
    print(f"Square Area: {square.area()}")
    print(f"Square Perimeter: {square.perimeter()}")