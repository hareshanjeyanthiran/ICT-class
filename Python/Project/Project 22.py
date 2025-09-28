num = int(input("Enter a number: "))

if num == 0:
    print("No set bits in 0")
else:
    position = 1       
    temp = num         

    while temp >0 :
        if temp % 2 == 1:   
            print("The position of the rightmost set bit is:", position)
            break
        else:
            temp = temp // 2  
            position += 1
