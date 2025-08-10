def check_prime(n):
    if(n<=1):
        return False
    
    for i in range(2,n):
        if n%i == 0:
            return False
            break

    return True


number = int(input("Enter your number: "))
if(check_prime(number)):
    print("It's a prime number")
else:
    print("It's not a prime number")