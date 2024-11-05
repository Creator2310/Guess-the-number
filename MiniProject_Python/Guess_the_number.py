import tkinter as tk
from tkinter import messagebox
import random

class GuessTheNumberGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Guess the Number Game")
        self.root.geometry("350x350")
        self.root.configure(bg="#f0f0f0")

        # Generate a random number between 1 and 100
        self.target_number = random.randint(1, 100)

        # Initialize attempts counter and scores
        self.attempts = 0
        self.scores = []

        # GUI components
        self.title_label = tk.Label(root, text="Guess the Number Game", font=("Arial", 16), bg="#f0f0f0")
        self.title_label.pack(pady=10)

        self.instruction_label = tk.Label(root, text="Guess a number between 1 and 100:", bg="#f0f0f0")
        self.instruction_label.pack(pady=5)

        self.guess_entry = tk.Entry(root, font=("Arial", 14))
        self.guess_entry.pack(pady=5)

        self.check_button = tk.Button(root, text="Check Guess", command=self.check_guess, bg="#4CAF50", fg="white", font=("Arial", 12))
        self.check_button.pack(pady=10)

        self.result_label = tk.Label(root, text="", bg="#f0f0f0", font=("Arial", 12))
        self.result_label.pack(pady=5)

        # Label to display the number of attempts
        self.attempts_label = tk.Label(root, text="Attempts: 0", bg="#f0f0f0", font=("Arial", 12))
        self.attempts_label.pack(pady=5)

        # Scores list display
        self.scores_label = tk.Label(root, text="Scores: []", bg="#f0f0f0", font=("Arial", 12))
        self.scores_label.pack(pady=5)

    def check_guess(self):
        try:
            guess = int(self.guess_entry.get())
            self.attempts += 1
            self.attempts_label.config(text=f"Attempts: {self.attempts}")

            if guess < self.target_number:
                self.result_label.config(text="Too low! Try again.")
            elif guess > self.target_number:
                self.result_label.config(text="Too high! Try again.")
            else:
                self.scores.append(self.attempts)
                if len(self.scores) > 5:
                    self.scores = self.scores[-5:]  # Keep only the last 5 scores
                messagebox.showinfo("Congratulations!", f"Correct! You guessed it in {self.attempts} attempts.")
                self.update_scores_label()
                self.reset_game()
        except ValueError:
            messagebox.showwarning("Invalid Input", "Please enter a valid number.")
        
        # Clear the input field after each guess
        self.guess_entry.delete(0, tk.END)

    def update_scores_label(self):
        self.scores_label.config(text=f"Scores: {self.scores}")

    def reset_game(self):
        self.target_number = random.randint(1, 100)
        self.attempts = 0
        self.guess_entry.delete(0, tk.END)
        self.result_label.config(text="")
        self.attempts_label.config(text="Attempts: 0")

# Create the main window
root = tk.Tk()
game = GuessTheNumberGame(root)
root.mainloop()
