#Armstrong Numbers
def armstrong(num):
    digit = str(num)
    power = len(digit)
    total = sum(int(d) ** power for d in digit)
    if num == total :
        print("This is a armstrong number")
    else:
        print("This is not an armstrong number")

user = int(input("Enter your number: "))
armstrong(user)