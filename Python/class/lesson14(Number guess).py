from tkinter import *
import random
screen = Tk()
screen.title("Number Guessing Game")
screen.geometry("400x300")
screen.config(bg="cyan")
header = Label(screen, text="Number Guessing Game", font=("Comic Sans MS", 18), fg="darkblue", bg="cyan")
header.pack(pady=10)
rule = Label(screen, text="Guess a number between 1 and 10", font=("Arial", 12), bg="cyan")
rule.pack(pady=5)
entry = Entry(screen, font=("Arial", 14, "bold"), bg="white", fg="black",bd=2,justify='center',relief='solid',)
entry.pack(pady=5)
random_number = random.randint(1, 10)

def reset_game():
    global random_number
    random_number = random.randint(1, 10)
    entry.delete(0, END)
    result_label.config(text="", bg="lightgreen", fg="black")
def check_guess():
    try:
        guess = int(entry.get())
        if guess < 1 or guess > 10:
            result_label.config(text="Please enter a number between 1 and 10", fg="red")
            return
        if guess == random_number:
            result_label.config(text="Congratulations! You guessed it right!", fg="black", bg="lightgreen")
        else:
            result_label.config(text=f"Wrong guess! The number was {random_number}", fg="black", bg="red")
    except ValueError:
        result_label.config(text="Please enter a valid number", fg="red")
check = Button(screen, text="Check guess", font=("Arial", 12), bg="blue", fg="white", command=check_guess)
check.pack(pady=5)
reset = Button(screen, text="Play again", font=("Arial", 12), bg="red", fg="white", command=reset_game)
reset.pack(pady=5)
result_label = Label(screen, text="", font=("Arial", 12), bg="lightgreen")
result_label.pack(pady=10)
screen.mainloop()