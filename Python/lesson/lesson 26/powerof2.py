#Program check if the number power of 2

def power2(number):
    #As the power of 2 will have only one set of bit,then n-1 & n will always be 0 for any power of 2
    if (number == 0):
        return 0
    if ((number & (~(number - 1))) == number):
        return 1
    return 0


number = int(input("Enter the number : "))

if(power2(number)):
    print("\n The number is a power of 2")
else:
    print("\n The number is not power of 2")
