def user(player):
    """
    Function to get a number from the user.
    """
    while True:
        try:
            choice = int(input(f"Player {player}, please enter an integer between 1, 2 and 3: "))
            if 1 <= choice <= 3:
                return choice
            else:
                print("The number must be between 1, 2 and 3.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
"""user_choice = user(input("Enter player numbers: "))
print(f"Player 1 chose: {user_choice}")"""
def play():
    sum = 0
    current_player = 1

    print("Welcome to the Number Game!")
    print("Players take turns to choose a number between 1 and 3.")
    print("The player to reach a total of 21 lose!")
    print("Let's start!")
    while True:
        print(f"Current total: {sum}")
        choice = user(f"Player {current_player}")
        sum += choice
        print(f"Current total: {sum}")

        if sum >= 21:
            print(f"Player {current_player} loses!")
            break

        # Switch players
        current_player = 2 if current_player == 1 else 1
play()