import tkinter as tk
from tkinter import ttk, messagebox
import pygame
import threading
import time

# 🎵 Play alert sound
def play_sound():
    pygame.mixer.init()
    pygame.mixer.music.load("alert.wav")  # alert.wav must be in the same folder
    pygame.mixer.music.play()

# 🔴 Blinking red text function
def blink_warning():
    current_color = virus_label.cget("fg")
    new_color = "#0d0d0d" if current_color == "red" else "red"
    virus_label.config(fg=new_color)
    virus_label.after(500, blink_warning)  # blink every 500 ms

# 🦠 Simulate virus scanning
def scan_for_virus():
    scan_button.config(state="disabled")
    progress_label.config(text="Scanning for viruses... 🧪")
    progress_bar.pack(pady=10)

    for i in range(101):
        progress_bar['value'] = i
        root.update_idletasks()
        time.sleep(0.02)

    progress_bar.pack_forget()
    progress_label.config(text="")
    virus_label.pack(pady=20)

    # 🔊 Play sound + blinking effect

    blink_warning()
    messagebox.showwarning("🛑 WARNING", "🦠 Stop! Virus Found.")

    scan_button.config(state="normal")

# Start scan in a new thread
def start_scan():
    threading.Thread(target=scan_for_virus).start()

# 🪟 Window setup
root = tk.Tk()
root.title("🛡️ Advanced Virus Scanner")
root.geometry("500x350")
root.configure(bg="#0d0d0d")

# 🏷️ Title
title = tk.Label(root, text="🛡️ Virus Scanner", font=("Helvetica", 20, "bold"), fg="#00ffaa", bg="#0d0d0d")
title.pack(pady=30)

# 🔘 Button
scan_button = tk.Button(
    root,
    text="🔍 Scan for the Virus",
    font=("Arial", 14, "bold"),
    bg="#ff1a1a",
    fg="white",
    activebackground="#cc0000",
    activeforeground="white",
    relief="flat",
    padx=20,
    pady=10,
    command=start_scan
)
scan_button.pack()

# 🔁 Progress bar
progress_label = tk.Label(root, text="", font=("Arial", 12), bg="#0d0d0d", fg="#ffffff")
progress_label.pack()

progress_bar = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
progress_bar.pack_forget()

# ⚠️ Blinking virus warning (initially hidden)
virus_label = tk.Label(
    root,
    text="⚠️ VIRUS DETECTED! ⚠️",
    font=("Arial", 18, "bold"),
    fg="red",
    bg="#0d0d0d"
)
virus_label.pack_forget()

# ▶️ Start main loop
root.mainloop()
