class car:
    seat = 4
    Engiene = 1
    Window = 5
    Brake = 1
    Acelerator = 1

    def __init__(self, color, model, Price):
        self.color = color
        self.model = model
        self.Price = Price

    def start(self):
        print(f"The {self.color} {self.model} car is starting.")

    def stop(self):
        print(f"The {self.color} {self.model} car is stopping.")

Toyota = car("Red", "Cruiser","$30,000")
Honda = car("Blue", "Civic", "$20,000")
#Toyota
print(Toyota.model)
print(Toyota.color)
print(Toyota.Price)
print(Toyota.seat)
print(Toyota.Window)
print(Toyota.Brake)
print(Toyota.Acelerator)
print(Toyota.start())
print(Toyota.stop())
#Honda
print(Honda.model)
print(Honda.color)
print(Honda.Price)
print(Honda.seat)
print(Honda.Window)
print(Honda.Brake)
print(Honda.Acelerator)
print(Honda.start())
print(Honda.stop())

class human:
    eyes = 2
    nose = 1
    ear = 2
    mouth = 1
    hand = 2

    def __init__(self, name, age, Gender, height, language):
        self.name = name
        self.age = age
        self.Gender = Gender
        self.height = height
        self.language = language

    def speak(self):
        print(f"{self.name} is speaking.")

    def walk(self):
        print(f"{self.name} is walking.")

    def Myself(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Height: {self.height}")
        print(f"Gender: {self.Gender}")
        print(f"Language: {self.language}")

Iham = human("Iham", 11, "Male", "4feet 8inches", "Urdu")
sam = human("Sam", 12, "Male", "4feet 9inches", "English")

# Iham
print(Iham.Myself())
print(Iham.speak())
print(Iham.walk())

# Sam
print(sam.Myself())
print(sam.speak())
print(sam.walk())