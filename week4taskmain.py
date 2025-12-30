# Taking input from the user for arithmetic operations
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("\nArithmetic Operations:")
print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)
print("Division:", num1 / num2)

print("\n----------------------\n")

# Taking input for different data types
name = input("Enter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height: "))
is_student = input("Are you a student? (True/False): ") == "True"

print("\nUser Details:")
print("Name:", name, "| Type:", type(name))
print("Age:", age, "| Type:", type(age))
print("Height:", height, "| Type:", type(height))
print("Is Student:", is_student, "| Type:", type(is_student))
