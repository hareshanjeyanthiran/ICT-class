#Denomination Calculator
from tkinter import *
screen = Tk()
screen.title("Denomination Calculator")
screen.geometry("400x400")
screen.config(bg="lightblue")
ins = Label(screen, text="Enter the total amount in dollars", bg="lightblue", font=("Arial", 14,"bold"))
ins.pack(pady=10)
amount = Entry(screen, width=20, font=("Arial", 12), justify="center", bg="#8fdfff", fg="#413636")
amount.pack(pady=5)
Calculate = Button(screen, text="Calculate", font=("Arial", 12, "bold"), bg="#68a7c0", fg="#595353", command=lambda: calculate_denomination(float(amount.get())))
Calculate.pack(pady=5)
result = Label(screen, text="", bg="lightblue", font=("Arial", 12, "bold"))
result.pack(pady=10)

def calculate_denomination(amount):
    denominations = [100, 50, 20, 10, 5, 1]
    result_text = "Denominations:\n"
    for denom in denominations:
        count = amount // denom
        amount %= denom
        result_text += f"${denom}: {count}\n"
    result.config(text=result_text)
    


screen.mainloop()