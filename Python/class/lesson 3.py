# Loops
a = 5

while (a<10):
    print(a)
    a = a+1

print("Another example")
b = 10

while(b>5):
    print(b)
    print("Inside loop")
    b = b-1

print("Outside loop")

for i in range(1,11):
    print(i,"Hello")
#Remove numbers you can remove i in print

print("Sum")
sum = 0

for i in range(1,11):
    sum = sum + i

print(sum)