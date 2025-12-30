import math

# Program to calculate the area of different shapes

while True:  # Infinite loop until the user chooses to exit
    print("\nChoose a shape to calculate the area:")
    print("1. Rectangle")
    print("2. Triangle")
    print("3. Circle")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    # Conditional statements to handle user choice
    if choice == "1":  # Rectangle
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        area = length * width
        print("Area of the rectangle:", area)

    elif choice == "2":  # Triangle
        base = float(input("Enter the base of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        area = 0.5 * base * height
        print("Area of the triangle:", area)

    elif choice == "3":  # Circle
        radius = float(input("Enter the radius of the circle: "))
        area = math.pi * radius ** 2
        print("Area of the circle:", area)

    elif choice == "4":  # Exit the loop
        print("Exiting the program. Goodbye!")
        break  # Break statement exits the while loop

    else:  # Handle invalid input
        print("Invalid choice! Please enter a number between 1 and 4.")

# Example of using a for loop for repeated input
print("\nNow let's calculate areas of multiple rectangles using a for loop:")
num_rectangles = int(input("How many rectangles do you want to calculate? "))

for i in range(num_rectangles):  # for loop iterates a fixed number of times
    print(f"\nRectangle {i+1}:")
    length = float(input("Enter the length: "))
    width = float(input("Enter the width: "))
    area = length * width
    print("Area:", area)
