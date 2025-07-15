import tkinter as tk
from tkinter import messagebox
import random

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.board = [" " for _ in range(9)]
        self.button = []
        for i in range(9):
            button = tk.Button(root, text="", font=("New Times Roman", 24), width=5, height=2,
                               command=lambda i=i: self.make_move(i))
            button.grid(row=i // 3, column=i % 3)
            self.button.append(button)

    def make_move(self, square):
        if self.board[square] == " ":
            self.board[square] = "x"
            self.button[square].config(text="x", state="disabled")
            if not self.check_winner("x"):
                self.computer_move()

    def computer_move(self):
        empty = [i for i, v in enumerate(self.board) if v == " "]
        if empty:
            move = random.choice(empty)
            self.board[move] = "o"
            self.button[move].config(text="o", state="disabled")
            self.check_winner("o")

    def check_winner(self, letter):
        # check rows
        for i in (0, 3, 6):
            if all(self.board[j] == letter for j in range(i, i + 3)):
                self.end_game(f"{letter.upper()} wins!")
                return True
        # check columns
        for i in range(3):
            if all(self.board[j] == letter for j in range(i, 9, 3)):
                self.end_game(f"{letter.upper()} wins!")
                return True
        # check diagonals
        if all(self.board[i] == letter for i in [0, 4, 8]) or all(self.board[i] == letter for i in [2, 4, 6]):
            self.end_game(f"{letter.upper()} wins!")
            return True
        # check for draw
        if " " not in self.board:
            self.end_game("It's a draw!")
            return True
        return False

    def end_game(self, message):
        messagebox.showinfo("Game Over", message)
        for btn in self.button:
            btn.config(state="disabled")
        print("Would you like to play again? (Yes/No)")

        response = input().strip().lower()
        if response == "yes":
            self.reset_game()
        else:
            print("Thanks for playing!")
        self.root.quit()
    def reset_game(self):
        self.board = [" " for _ in range(9)]
        for btn in self.button:
            btn.config(text="", state="normal")


if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()