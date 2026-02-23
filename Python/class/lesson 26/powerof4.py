#Program to check if a number is power of 4
def powerof4(number):

    count = 0

    #if only one set bit exists
    if (number & (~(number & (number - 1)))):

        #count 0 bits before set bit
        while(number > 1):
            number >>= 1
            count += 1

        #If count even return true else false 
        if(count % 2 == 0):
            return True
        else:
            return False
        
number = int(input("Enter your number : "))
if(powerof4(number)):
    print("Number is a power of 4")
else:
    print("Number is not a power of 4")