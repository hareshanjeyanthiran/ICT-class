class Expression:
    def __init__(self, num1, num2, num3):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3

    def add_numbers(self):
        result = self.num1 + self.num2 + self.num3
        print("The sum is:", result)


expr1 = Expression(5, 10, 15)
expr2 = Expression(2, 4, 6)


expr1.add_numbers()
expr2.add_numbers()