#Meghan is a college student, and she has to create to update a different password every week when she logs into her college website dashboard. Thinking of a different password every week can be a tedious task, so she is thinking of creating a Python program that can help her to generate different passwords. Help her create a Random Password Generator that returns passwords composed of lowercase letters, uppercase letters, digits, and punctuations using  tkinter also give more colour and a text box then enter button reset button to show red text with You are wrong and green text with You are correct and start to make.
from tkinter import *
import random
import string
def generate_password():
    length = int(length_entry.get())
    if length < 4:
        result_label.config(text="You are wrong", fg="red")
        return
    
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    
    result_label.config(text=f"Generated Password: {password}", fg="green")

def reset():
    length_entry.delete(0, END)
    result_label.config(text="", fg="black")

# Create the main window
root = Tk()
root.title("Random Password Generator")
root.geometry("400x300")
root.configure(bg="lightblue")
Label(root, text="Enter Password Length:", bg="lightblue", font=("Arial", 12)).pack(pady=10)
length_entry = Entry(root, font=("Arial", 12), justify="center", relief="groove")
length_entry.pack(pady=5)
generate_button = Button(root, text="Generate Password", command=generate_password, bg="green", fg="white", font=("Arial", 12), justify="center")
generate_button.pack(pady=10)
reset_button = Button(root, text="Reset", command=reset, bg="red", fg="white", font=("Arial", 12), justify="center")
reset_button.pack(pady=5)
result_label = Label(root, text="", bg="lightblue", font=("Arial", 12), justify="center")
result_label.pack(pady=10)
root.mainloop()