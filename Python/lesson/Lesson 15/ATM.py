print("Welcome to ATM security system")
print("Members who logged in are:")
import time
from tkinter import *
screen = Tk()
screen.geometry("500x450")
screen.title("ATM")
screen.config(bg="gray")
title = Label(screen, text="Welcome to ATM", font=("Arial", 17, "bold",), bg="lightblue", fg="black", padx=10, pady=10, borderwidth=2, relief="groove")#Do Border curve plz
title.pack(pady=20)
#Pin
instruction = Label(screen, text="Enter your 4 digit PIN", font=("Arial", 12), bg="gray", fg="black")
instruction.pack(pady=10)
#Entry for PIN
pin_entry = Entry(screen, font=("Arial", 14), width=20, show="*", justify="center", borderwidth=2, relief="groove")
pin_entry.pack(pady=7)
#Button to submit PIN
submit_button = Button(screen, text="Enter", font=("Arial", 12), bg="lightblue", fg="black", padx=10, pady=5, borderwidth=2, relief="groove")
submit_button.pack(pady=20)
#Button to exit
exit_button = Button(screen, text="Exit", font=("Arial", 12), bg="lightcoral", fg="black", padx=10, pady=5, borderwidth=2, relief="groove", command=screen.quit)
exit_button.pack(pady=10)
# Run the application
user_pin = {
    "1234": "Hareshan",
    "5678": "Kartik",
    "9101": "Jileshan"
}



def on_submit():
    pin = pin_entry.get()
    if len(pin) == 4 and pin.isdigit():
        if pin in user_pin:
            print(f"{user_pin[pin]} is logged in successfully  Time: {time.strftime('%Y-%m-%d %H:%M:%S')}")
            output_label.config(text=f"Welcome {user_pin[pin]}", bg="lightgreen", fg="black")
        else:
            output_label.config(text="Invalid PIN. Please enter a 4-digit number.",bg="red", fg="black")
            print("A person with this PIN is not registered   pin:", pin,  "  Time:",time.strftime('%Y-%m-%d %H:%M:%S'))

submit_button.config(command=on_submit)

output_label = Label(screen, text="", font=("Arial", 12), bg="gray", fg="black")
output_label.pack(pady=10)


screen.mainloop()