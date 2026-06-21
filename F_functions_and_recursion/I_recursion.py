# # Recursion

# When a function calls itself repeatedly

# Example: prints n to 1 backwards

def show(n):
    # Base Case - Stops the recursion
    if n == 0:
        return
    print(n)
    show(n - 1)  # Recursive call with smaller value

# --- Additional Revision Notes ---

# 1. Understanding Recursion - The Complete Picture:

# Recursion has two essential parts:
# 1. Base Case: The condition that stops the recursion (prevents infinite loop)
# 2. Recursive Case: The function calling itself with a smaller/ simpler input

# 2. How the example works:
def show(n):
    if n == 0:           # BASE CASE: Stop when n reaches 0
        return
    print(n)             # Print current number
    show(n - 1)          # RECURSIVE CASE: Call with n-1

# When you call show(5):
# show(5) prints 5, calls show(4)
# show(4) prints 4, calls show(3)
# show(3) prints 3, calls show(2)
# show(2) prints 2, calls show(1)
# show(1) prints 1, calls show(0)
# show(0) hits base case and returns (stops)

# Output: 5, 4, 3, 2, 1

# 3. Print numbers from 1 to n (forward):
def show_forward(n):
    if n == 0:
        return
    show_forward(n - 1)   # Recursive call FIRST
    print(n)              # Then print

# When you call show_forward(5):
# show_forward(5) calls show_forward(4)
# show_forward(4) calls show_forward(3)
# show_forward(3) calls show_forward(2)
# show_forward(2) calls show_forward(1)
# show_forward(1) calls show_forward(0)
# show_forward(0) hits base case and returns
# Then unwinds: prints 1, then 2, then 3, then 4, then 5

# Output: 1, 2, 3, 4, 5

# 4. Factorial using Recursion:
def factorial(n):
    # Base case
    if n == 0 or n == 1:
        return 1
    # Recursive case
    return n * factorial(n - 1)

print(factorial(5))  # Output: 120

# How factorial(5) works:
# factorial(5) = 5 * factorial(4)
# factorial(4) = 4 * factorial(3)
# factorial(3) = 3 * factorial(2)
# factorial(2) = 2 * factorial(1)
# factorial(1) = 1 (base case)
# Then unwinds: 5*4*3*2*1 = 120

# 5. Sum of first n natural numbers using Recursion:
def sum_numbers(n):
    if n == 0:
        return 0
    return n + sum_numbers(n - 1)

print(sum_numbers(5))  # 5+4+3+2+1 = 15

# 6. Fibonacci Series using Recursion:
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(6))  # Output: 8 (0,1,1,2,3,5,8)

# 7. Power function using Recursion:
def power(base, exp):
    if exp == 0:
        return 1
    return base * power(base, exp - 1)

print(power(2, 5))   # 2^5 = 32

# 8. Recursion vs Iteration:

# Using Loop (Iterative):
def factorial_iterative(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

# Using Recursion:
def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)

# Both give same result, but approach is different

# 9. Important Rules for Recursion:

# a) Always have a BASE CASE (to stop recursion)
# b) Recursive call must move TOWARDS the base case
# c) Each recursive call should solve a smaller/simpler problem

# 10. Common Recursion Patterns:

# Pattern 1: Head Recursion (process before recursion)
def head_recursion(n):
    if n == 0:
        return
    print(n)           # Process first
    head_recursion(n-1) # Then recurse

# Pattern 2: Tail Recursion (process after recursion)
def tail_recursion(n):
    if n == 0:
        return
    tail_recursion(n-1) # Recurse first
    print(n)            # Then process

# 11. Practical Example: Sum of digits using Recursion:
def sum_of_digits(n):
    if n == 0:
        return 0
    return (n % 10) + sum_of_digits(n // 10)

print(sum_of_digits(12345))  # 1+2+3+4+5 = 15

# 12. Reverse string using Recursion:
def reverse_string(s):
    if len(s) == 0:
        return ""
    return s[-1] + reverse_string(s[:-1])

print(reverse_string("hello"))  # "olleh"

# 13. Check palindrome using Recursion:
def is_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])

print(is_palindrome("racecar"))   # True
print(is_palindrome("hello"))     # False

# 14. Recursion vs Iteration Comparison:

# Iteration (Loop):
# + Faster
# + Uses less memory
# + Easier to understand for simple problems

# Recursion:
# + Cleaner code for complex problems
# + Easier to implement tree/graph traversal
# - Uses more memory (call stack)
# - Slower for large inputs
# - Risk of stack overflow for deep recursion

# 15. When to use Recursion:
# - Problems with tree/graph structures
# - Problems that can be divided into similar sub-problems
# - Backtracking problems (N-Queens, Maze)
# - Traversing nested structures
# - Problems where iterative solution is complex

# 16. Common Mistakes:

# Mistake 1: Forgetting base case
# def bad_recursion(n):
#     return n + bad_recursion(n-1)  # No base case! Infinite recursion!

# Mistake 2: Not moving towards base case
# def bad_recursion(n):
#     if n == 0:
#         return 0
#     return n + bad_recursion(n)  # n never decreases! Infinite!

# Mistake 3: Stack overflow for large numbers
# print(factorial(10000))  # RecursionError! Python recursion limit ~1000

# 17. Increasing recursion limit (use cautiously):
import sys
sys.setrecursionlimit(5000)  # Allows deeper recursion

# 18. Memoization - Making recursion faster:
# Cache results to avoid recomputation
def fibonacci_memo(n, cache={}):
    if n in cache:
        return cache[n]
    if n == 0:
        return 0
    if n == 1:
        return 1
    cache[n] = fibonacci_memo(n-1, cache) + fibonacci_memo(n-2, cache)
    return cache[n]

print(fibonacci_memo(50))  # Fast even for large numbers!

# 19. Recursion Visual Trace:
def trace_factorial(n, depth=0):
    indent = "  " * depth
    print(f"{indent}factorial({n}) called")
    if n == 0 or n == 1:
        print(f"{indent}Base case: return 1")
        return 1
    result = n * trace_factorial(n-1, depth+1)
    print(f"{indent}factorial({n}) returns {result}")
    return result

trace_factorial(4)

# Output shows the call stack and returns

# 20. Key Takeaway:
# Recursion is a powerful tool, but always:
# 1. Define base case FIRST
# 2. Ensure recursive call gets closer to base case
# 3. Consider if iteration would be simpler
# 4. Use memoization for expensive repeated calculations