from tkinter import *
screen = Tk()
screen.title("Virus Scanner")
screen.geometry("400x400")
screen.config(bg="black")

def start_scan():
    result.config(text="Scanning for viruses...", bg="black", fg="white", font=("Arial", 14))
    screen.after(2000, show_warning)

def show_warning():
    result.config(text="⚠️Bug found! Virus detected!", bg="red", fg="white", font=("Arial", 24))


scan = Button(screen, text="Scan", command=start_scan, bg="green", fg="white", font=("Arial", 14))
scan.pack(pady=20)
result = Label(screen, text="", bg="black", fg="white")
result.pack(pady=20)



screen.mainloop()
