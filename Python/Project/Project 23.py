def power(num):
    if num <= 0:
        return False
    while num % 8 == 0:
        num //= 8
    return num == 1

# Test the function
number = int(input("Enter a number: "))
if power(number):
    print(f"{number} is a power of 8.")
else:
    print(f"{number} is not a power of 8.")