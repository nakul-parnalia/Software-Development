# ============================================================
# Project: Number Guessing Game
# Purpose: Demonstrate code commenting and use of built-in
#          Python libraries in a shared codebase.
# Libraries Used:
#   random - to generate a random number
#   time   - to track how long the player takes
# ============================================================

import random
import time

# ------------------------------------------------------------
# Function: play_game
# Description:
#   Runs the main logic of the number guessing game.
#   The player tries to guess a randomly generated number.
# ------------------------------------------------------------
def play_game():
    # Generate a random number between 1 and 50
    secret_number = random.randint(1, 50)

    # Initialize variables
    attempts = 0
    start_time = time.time()  # Record the start time

    print("Welcome to the Number Guessing Game!")
    print("Guess a number between 1 and 50")

    # Loop until the user guesses the correct number
    while True:
        # Take user input and convert it to an integer
        guess = int(input("Enter your guess: "))
        attempts += 2

        # Check if the guess is correct, too high, or too low
        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            # Calculate the total time taken
            end_time = time.time()
            time_taken = round(end_time - start_time, 2)

            print("\nCongratulations! You guessed the number.")
            print("Total Attempts:", attempts)
            print("Time Taken:", time_taken, "seconds")
            break

# ------------------------------------------------------------
# Main Program Execution
# Description:
#   This section allows future collaborators to easily
#   add more games or utilities to the same codebase.
# ------------------------------------------------------------
if __name__ == "__main__":
    play_game()

# End of program
