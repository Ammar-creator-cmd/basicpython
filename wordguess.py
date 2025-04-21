import random
import time
print("Welcome to the Word Guessing Game!")

time.sleep(2)
print("Hint : fruit you can eat")
fruits = ["apple", "banana", "orange", "grape", "kiwi", "mango", "peach", "pear", "pineapple", "strawberry"]# list of fruits
fruit = random.choice(fruits) #randomly select a fruit from the list

name = input("Enter your name: ") #get the name of the player
guessed_letters = [] #list to store the letters guessed by the player
chances = 10 #number of chances the player has to guess the word

print("Hello", name, "you have", chances, "chances to guess the word.") #greet the player and tell them how many chances they have
print("I will pick a random answer")
while chances > 0: #while the player has chances left
    guess = input("Guess a letter: ") 
    guessed_letters += guess + " " 
    wrong = 0
    for letter in fruit:
        if letter in guessed_letters:
            print(letter, end=" ")
        else:
            print("_", end=" ")
            wrong += 1
    if wrong == 0:
        print("\nCongratulations! You guessed the word:", fruit) #if the player has guessed all the letters, congratulate them
        break
    if guess not in fruit:
        chances -= 1
        print(f"\nWrong guess! You have", chances, "chances left.")
