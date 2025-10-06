#Program to find the number of bits needed to be swapped to make 2 equal number

def totalflips(number1,number2):

    #Variable to count flips requierd
    flips = 0

    #Get the last bit of both numbers and check of both are same if yes no flip
#requiered else flip is required
    while(number1 > 0 or number2 > 0):
        t1 = (number1 & 1)
        t2 = (number2 & 1)
        if(t1 != t2):
            flips += 1

        #Right shift both numbers
        number1>>=1
        number2>>=1
    
    return flips


number1 = int(input("Input first number : "))
number2 = int(input("Input second number : "))
 
print("\n number of flips needed : ",totalflips(number1,number2))
