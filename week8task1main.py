# ============================================================
# Recursion Examples in Python
# Demonstrates factorial, Fibonacci sequence, and sum of numbers
# ============================================================

# ----------------- Factorial -----------------
def factorial(n):
    """
    Returns the factorial of n using recursion.
    Base case: factorial(0) = 1
    Recursive case: n! = n * factorial(n-1)
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# ----------------- Fibonacci -----------------
def fibonacci(n):
    """
    Returns the nth Fibonacci number using recursion.
    Base case: fibonacci(0) = 0, fibonacci(1) = 1
    Recursive case: F(n) = F(n-1) + F(n-2)
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# ----------------- Sum of Natural Numbers -----------------
def sum_natural(n):
    """
    Returns the sum of first n natural numbers using recursion.
    Base case: sum_natural(1) = 1
    Recursive case: sum_natural(n) = n + sum_natural(n-1)
    """
    if n == 1:
        return 1
    else:
        return n + sum_natural(n - 1)

# ----------------- Main Program -----------------
# Factorial
num = int(input("Enter a number to calculate factorial: "))
print(f"Factorial of {num} is {factorial(num)}\n")

# Fibonacci
terms = int(input("Enter number of terms for Fibonacci sequence: "))
print("Fibonacci sequence:")
for i in range(terms):
    print(fibonacci(i), end=" ")
print("\n")

# Sum of Natural Numbers
n = int(input("Enter a number to calculate sum of first n natural numbers: "))
print(f"Sum of first {n} natural numbers is {sum_natural(n)}")
