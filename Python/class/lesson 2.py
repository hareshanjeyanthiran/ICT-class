age = 10 

if age>18:
    print("Hey you can drive")
else:
    print("Sorry you have to wait")

day = 100

if day == 1 :
    print("Sunday")
elif day == 2 :
    print("Monday")
elif day == 3 :
    print("Tuesday")
elif day == 4 :
    print("Wednesday")
elif day == 5 :
    print("Thursday")
elif day == 6 :
    print("Friday")
elif day == 7 :
    print("Saterday")
else:
    print("Invalid!!!")

username = "Cooldriver"
passcode = 1234

if username == "Cooldrive" :
    if passcode == 1234:
        print("Welcome")
    else:
        print("Incorrect passcode")
else:
    print("Incorrect username")

age = 2
Result = "Hey you can vote" if age>18 else "Sorry"
print(Result)

#Date and Time

from datetime import datetime ,date,time
Date_Time = datetime.now()
Date2 = datetime.now().date()
Time = datetime.now().time()
Date = date.today()

print(Date)
print(Time)
print(Date_Time)
print(Date2)