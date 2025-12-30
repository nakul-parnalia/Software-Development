# ============================================================
# Topic: Introduction to Python Functions
# Purpose: Demonstrate real-world use of functions, parameters,
#          return values, and function reusability in one program
# ============================================================

# Function 1: Greet a user (real-world scenario: welcoming users)
def greet_user(name):
    print("Hello", name, "- Welcome!")

# Function 2: Calculate total bill (real-world scenario: shopping)
def calculate_bill(price, tax_rate):
    total = price + (price * tax_rate)
    return total

# Function 3: Convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# ---------------- Main Program ----------------

# Using greet function
user_name = input("Enter your name: ")
greet_user(user_name)

# Using bill calculation function
price = float(input("Enter item price: "))
tax = float(input("Enter tax rate (e.g., 0.05 for 5%): "))
total_bill = calculate_bill(price, tax)
print("Total Bill Amount:", total_bill)

# Using temperature conversion function
temp_celsius = float(input("Enter temperature in Celsius: "))
temp_fahrenheit = celsius_to_fahrenheit(temp_celsius)
print("Temperature in Fahrenheit:", temp_fahrenheit)

# ------------------------------------------------
# This single program demonstrates:
# - Function definition
# - Parameters
# - Return values
# - Reusability of functions
# ============================================================
