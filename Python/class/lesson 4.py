#Functions
#Storing functions like print
# Example:
def greet():
    print("Hi")

greet()

def GM():
    print("Good morning")

def GN():
    print("Good night")

GN()
GM()

#Parametor
# Example:
def Hi(name):
    print("Hi",name)

name = input("Enter your name: ")
Hi(name)

def SP(sport):
    print("Your sport is ",sport)

sport = input("Enter your sport: ")
SP(sport)

#Calculator
def add():
    print(a+b)
def sub():
    print(a-b)
def mul():
    print(a*b)
def div():
    print(a/b)

print("Chose one of these")
print("1 Addition")
print("2 Subtraction")
print("3 Multiplication")
print("4 Division")

choise = int(input())
a = int(input("Enter first digit: "))
b = int(input("Enter second digit: "))

if choise==1:
    add()
elif choise==2:
    sub()
elif choise==3:
    mul()
elif choise==4:
    div()
else:
    print("Ïnvalid")

#Callback

def draw(callback):
    print("Drawing the picture")
    callback()
 
def show():
    print("Showing picture")

draw(show)