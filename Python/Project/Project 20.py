def lcm(a, b):
    if a > b:
        greater = a
   
    while True:
        if (greater % a == 0) and (greater % b == 0):
            return greater
        greater += 1

large = int(input("Enter the large number: "))
small = int(input("Enter the small number: "))

if large > small :
    print("The LCM of", large, "and", small, "is", lcm(large, small))
else:
      print("Enter your number using the correct statement")
      large = int(input("Enter the large number: "))
      small = int(input("Enter the small number: "))