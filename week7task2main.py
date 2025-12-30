import random

# Generate a random number between 1 and 50
secret_number = random.randint(1, 50)

# Maximum number of attempts
max_attempts = 5

print("Welcome to the Number Guessing Game!")
print(f"You have {max_attempts} attempts to guess the number between 1 and 50.")

# Loop exactly for 5 attempts
for attempt in range(1, max_attempts + 1):
    guess = int(input(f"Attempt {attempt}: Enter your guess: "))

    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print(f"Congratulations! You guessed the number {secret_number} in {attempt} attempts.")
        break
else:
    # This executes if all attempts are used without a correct guess
    print(f"Sorry! You've used all {max_attempts} attempts. The number was {secret_number}.")
