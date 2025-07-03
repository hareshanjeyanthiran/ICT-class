import datetime;
from tkinter import *;
screen = Tk();
screen.title("Age Calculator");
screen.geometry("350x250");
screen.config(bg="lightblue");
header = Label(screen, text="Age Calculator", font=("Arial", 18),fg="crimson", bg="lightblue");
header.pack(pady=10);
age_label = Label(screen, text="Enter your Birth Year:", font=("Arial", 10), bg="lightblue");
age_label.pack(pady=5);

age_box = Entry(screen, font=("Arial", 14));
age_box.pack(pady=5);

def calculate_age():
    birth_year = age_box.get()
    if birth_year=="":
        result_label.config(text="Please enter a valid year.");
    else:
        birth_year = int(age_box.get());
        current_year = datetime.datetime.now().year;
        age = current_year - birth_year;
        if age <= 0:
            result_label.config(text="You haven't been born yet!");
        else:
            result_label.config(text=f"Your age is: {age} years");

cal = Button(screen, text="Calculate Age", font=("Arial", 10), bg="crimson", fg="white", command=calculate_age);
cal.pack(pady=10);

result_label = Label(screen, text="", font=("Arial", 12), bg="lightblue");
result_label.pack(pady=10);
screen.mainloop();