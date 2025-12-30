# ============================================================
# Optimized Fibonacci Calculator with Memoization
# ============================================================

# Dictionary to store previously computed Fibonacci numbers
memo = {}

def fibonacci_recursive(n):
    """
    Basic recursive Fibonacci function.
    Base cases: fibonacci_recursive(0) = 0, fibonacci_recursive(1) = 1
    Recursive case: F(n) = F(n-1) + F(n-2)
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

def fibonacci_memo(n):
    """
    Optimized Fibonacci using memoization.
    Stores previously computed results in a dictionary to avoid redundant calculations.
    """
    if n in memo:
        return memo[n]
    if n == 0:
        result = 0
    elif n == 1:
        result = 1
    else:
        result = fibonacci_memo(n - 1) + fibonacci_memo(n - 2)
    
    memo[n] = result  # Store result in memo dictionary
    return result

# ----------------- Main Program -----------------
n_terms = int(input("Enter the number of terms in the Fibonacci sequence: "))

print("\nFibonacci sequence using basic recursion:")
for i in range(n_terms):
    print(fibonacci_recursive(i), end=" ")

print("\n\nFibonacci sequence using memoization:")
for i in range(n_terms):
    print(fibonacci_memo(i), end=" ")

print("\n\nNotes:")
print("1. Basic recursion is simple but slow for large n due to repeated calculations.")
print("2. Memoization stores results to make recursion efficient, avoiding redundant work.")
