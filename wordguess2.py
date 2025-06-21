import random
import time
print("Welcome to the Word Guessing Game!")
time.sleep(2)
print("Hint: Current Arsenal FC Players")
players = [
    "saka", "odegaard", "martinelli", "jesus", "saliba", 
    "rice", "trossard", "jorginho", "white",
    "zinchenko", "gabriel", "kiwior", "setford", "neto"
]  # list of Arsenal FC players

player = random.choice(players)  # randomly select a player from the list
name = input("Enter your name: ")
print(f"Hello {name}, let's start the game!")
guessed_letters = []  
chances = 10  
print(f"You have {chances} chances to guess the player's name.")
while chances > 0: #while the player has chances left
    guess = input("Guess a letter: ") 
    guessed_letters += guess + " " 
    wrong = 0
    for letter in player:
        if letter in guessed_letters:
            print(letter, end=" ")
        else:
            print("_", end=" ")
            wrong += 1
    if wrong == 0:
        print("\nCongratulations! You guessed the word:", fruit) #if the player has guessed all the letters, congratulate them
        break
    if guess not in player:
        chances -= 1
        print(f"\nWrong guess! You have", chances, "chances left.")
