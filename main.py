import tkinter as tk
from tkinter import messagebox
import random

# Function to handle the guessing logic
def check_guess():
    global attempts
    try:
        guess = int(entry_guess.get())
        attempts += 1
        if guess < number_to_guess:
            result_label.config(text="Too low! Try again.", fg="blue")
        elif guess > number_to_guess:
            result_label.config(text="Too high! Try again.", fg="blue")
        else:
            result_label.config(text=f"Congratulations! You guessed the number {number_to_guess} in {attempts} attempts.", fg="green")
            messagebox.showinfo("Success!", f"You've guessed the number {number_to_guess} in {attempts} attempts!")
            reset_game()
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")

# Function to reset the game
def reset_game():
    global number_to_guess, attempts
    number_to_guess = random.randint(1, 100)
    attempts = 0
    entry_guess.delete(0, tk.END)
    result_label.config(text="Guess a number between 1 and 100", fg="black")

# Initialize the main window
root = tk.Tk()
root.title("Guessing Game")
root.geometry("400x250")
root.resizable(False, False)

# Initialize game variables
number_to_guess = random.randint(1, 100)
attempts = 0

# Create GUI components
title_label = tk.Label(root, text="Welcome to the Guessing Game!", font=("Arial", 14), pady=10)
title_label.pack()

instruction_label = tk.Label(root, text="Guess a number between 1 and 100:", font=("Arial", 12))
instruction_label.pack()

entry_guess = tk.Entry(root, font=("Arial", 12), width=10)
entry_guess.pack(pady=10)

guess_button = tk.Button(root, text="Submit Guess", font=("Arial", 12), command=check_guess)
guess_button.pack(pady=5)

reset_button = tk.Button(root, text="Reset Game", font=("Arial", 12), command=reset_game)
reset_button.pack(pady=5)

result_label = tk.Label(root, text="Guess a number between 1 and 100", font=("Arial", 12), fg="black")
result_label.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
