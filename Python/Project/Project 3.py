print("Welcome to exam result pass or fail checker!!!!")
marks = int(input("Enter your marks:"))
if marks>=75:
    print("You Pass!!!")
elif marks<0:
    print("Invalid!")
elif marks<75:
    print("You faild")
else:
    print("Invalid!")