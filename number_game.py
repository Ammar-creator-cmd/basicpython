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
