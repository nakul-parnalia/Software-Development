# Importing built-in Python libraries
# math is used for mathematical operations
# random is used to generate random numbers
import math
import random

# This program generates a random number
# and performs mathematical calculations on it

# Generate a random integer between 1 and 10
random_number = random.randint(1, 10)

# Display the generated random number
print("Random Number Generated:", random_number)

# Calculate the square root of the number using math library
square_root = math.sqrt(random_number)

# Calculate the factorial of the number using math library
factorial = math.factorial(random_number)

# Display the calculated results
print("Square Root:", square_root)
print("Factorial:", factorial)

# This section performs additional calculations
# Rounding the square root value to 2 decimal places
rounded_value = round(square_root, 2)

# Display the rounded result
print("Rounded Square Root:", rounded_value)

# End of program
# This program demonstrates the use of comments
# and Python's built-in libraries
