class laptop:
    def __init__(self, name, color, price):
        self.name = name
        self.color = color
        self.price = price

    def showprice(self):
        print(f"The price of {self.name} is {self.price}")

    def showcolor(self):
        print(f"The color of {self.name} is {self.color}")
    
    def product(self):
        print(f"{self.name} is a {self.color} laptop and costs {self.price}")

hp = laptop("HP Pro Book", "Black", "$50000")
dell = laptop("Dell XPS", "Silver", "$60000")

hp.showprice()
hp.showcolor()
hp.product()

dell.showprice()
dell.showcolor()
dell.product()


print("Inheritance")
class A:
    x = 7

class B(A):
    pass

b = B()
print(b.x)  