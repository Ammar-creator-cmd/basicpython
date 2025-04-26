import random
import time

print("Welcome to the Word Guessing Game!")
time.sleep(2)
print("Hint: It's a type of insect.")
insects = ["ant", "bee", "beetle", "butterfly", "cockroach", "dragonfly", "grasshopper", "ladybug", "mosquito", ]

insect = random.choice(insects) 
name = input("Enter your name: ")
guessed_letters = []
chances = 10
print("Hello", name, "you have", chances, "chances to guess the word.")
print("I will pick a random answer")
while chances > 0:
    guess = input("Guess a letter: ")
    guessed_letters += guess + " "
    wrong = 0
    for letter in insect:
        if letter in guessed_letters:
            print(letter, end=" ")
        else:
            print("_", end=" ")
            wrong += 1
    if wrong == 0:
        print("\nCongratulations! You guessed the word:", insect)
        break
    if guess not in insect:
        chances -= 1
        print(f"\nWrong guess! You have", chances, "chances left.")
    if chances == 0:
        print("Sorry, you've run out of chances. The word was:", insect)