import tkinter as tk
import random

# Initialize main window
window = tk.Tk()
window.title("Guess the Number Game")
window.geometry("400x300")
window.config(bg="#e3f2fd")

# Generate a random number between 1 and 10
number = random.randint(1, 10)

# Function to handle guessing
def check_guess():
    global number
    try:
        guess = int(entry.get())
        if guess < 1 or guess > 10:
            result_label.config(text="⚠️ Number out of range! (1–10)", fg="orange")
        elif guess < number:
            result_label.config(text="Too low! Try again.", fg="blue")
        elif guess > number:
            result_label.config(text="Too high! Try again.", fg="purple")
        else:
            result_label.config(text="🎉 Correct! You guessed it!", fg="green")
            # Generate new number for another round
            number = random.randint(1, 10)
            entry.delete(0, tk.END)
    except ValueError:
        result_label.config(text="❌ Please enter a valid number!", fg="red")

# Title Label
title_label = tk.Label(window, text="🎮 Guess the Number!", font=("Arial", 18, "bold"), bg="#e3f2fd")
title_label.pack(pady=10)

# Instructions
instruction_label = tk.Label(window, text="I'm thinking of a number between 1 and 10.", bg="#e3f2fd", font=("Arial", 12))
instruction_label.pack()

# Entry box
entry = tk.Entry(window, font=("Arial", 14), justify="center")
entry.pack(pady=10)

# Guess Button
guess_button = tk.Button(window, text="Submit Guess", font=("Arial", 12, "bold"), bg="#42a5f5", fg="white", command=check_guess)
guess_button.pack(pady=10)

# Result Label
result_label = tk.Label(window, text="", bg="#e3f2fd", font=("Arial", 12))
result_label.pack(pady=10)

# Run the game
window.mainloop()
