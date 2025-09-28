def oneoddoccuring(arr):
    #Initalize result
    res = 0

    #Travers the arry
    for element in arr:
        #XOR with the resut
        res = res^element

    return res

#Initalize our arry
arr = []

#Take arry size as input
n = int(input("Enter array size: "))

#Take arry element input
while(n):
    num = int(input("Enter number : "))
    arr.append(num)
    n-=1

print("\n\nodd occurring number is : ",oneoddoccuring(arr))