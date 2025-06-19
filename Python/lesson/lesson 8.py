class Car :
    seat = 4
    Engine = "V8"
    Window = 5
    AC = True
   
    def Run(self):
        print("The Car is Running...")


bugati = Car()
ferrari = Car()

print(bugati.seat)
print(ferrari.Window)
print(bugati.Run())

class Human:
    eyes = 2
    nose = 1
    ear = 2
    mouth = 1
    hand = 2
    
Iham = Human()
sam = Human()
print(sam.eyes)

class vehicle:

    def __init__(self,color,Price,Engiene):
        self.color = color
        self.Price = Price
        self.Engiene = Engiene

mclaren = vehicle("Red","$1,000,000","F5")
BMW     = vehicle("Blue","$100,000","V5")

print(mclaren.color)
print(BMW.color)