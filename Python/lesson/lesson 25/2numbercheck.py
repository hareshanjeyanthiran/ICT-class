# Program to check if user input numbers are equal with out using any comparison operator

def checkifsame(number_1,number_2):

#User XOR operator as a^a is always 0
        if((number_1 ^ number_2) !=0):
                print("Numbers are equal")
        else:
                print("Both numbers are equal")

#Taking input
number1 = int(input("Enter first number to compare: "))
number2 = int(input("Enter second number to compare: "))

checkifsame(number1,number2)

