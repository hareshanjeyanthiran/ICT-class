import random
from tkinter import *
#Rock Paper Scissors Game
screen = Tk()
screen.title("Rock Paper Scissors")
screen.geometry("400x400")
screen.config(bg="lightblue")

def start_game():
    header.config(text="Choose your option:")
    start.pack_forget()  
    option1 = Button(screen, text="Rock", font=("Arial", 14), bg="lightgreen",command=lambda: choose_option("Rock"))
    option1.pack(pady=5)
    option2 = Button(screen, text="Paper", font=("Arial", 14), bg="lightgreen",command=lambda: choose_option("Paper"))
    option2.pack(pady=5)
    option3 = Button(screen, text="Scissors", font=("Arial", 14), bg="lightgreen",command=lambda: choose_option("Scissors"))
    option3.pack(pady=5)
    AI = Label(screen, text="AI Score = " + str(AI_score), font=("Arial", 12), bg="lightblue")
    AI.pack(pady=5)
    You = Label(screen, text="Your Score = " + str(You_score), font=("Arial", 12), bg="lightblue")
    You.pack(pady=5)
    AI_score = 0
    You_score = 0

    AI_score.config(text="AI Score = " + str(AI_score))
    You_score.config(text="Your Score = " + str(You_score))


def choose_option(choice):
        
        AI_choice = random.choice(["Rock", "Paper", "Scissors"])
        if choice == AI_choice:
            result = "It's a tie!"
        elif (choice == "Rock" and AI_choice == "Scissors") or \
             (choice == "Paper" and AI_choice == "Rock") or \
             (choice == "Scissors" and AI_choice == "Paper"):
            result = "You win!"
            You_score += 1
        else:
            result = "AI wins!"
            AI_score += 1
        result_label.config(text=f"You chose {choice}, AI chose {AI_choice}. {result}")
    







header = Label(screen, text="Rock Paper Scissors Game", bg="lightblue", font=("Arial", 16))
header.pack(pady=10)
start = Button(screen, text="Start Game", font=("Arial", 14), bg="lightgreen",command=start_game)
start.pack(pady=20)



result_label = Label(screen, text="", font=("Arial", 12), bg="lightblue")
result_label.pack(pady=10)






screen.mainloop()