# Functions in Python

# Block of statements that perform a specific task.

# Syntax:
# def func_name(param1, param2...):
#     # some work
#     return val

# func_name(arg1, arg2...)    # function call

# Example:
def sum(a, b):
    s = a + b
    return s

print(sum(2, 3))            # Output: 5

# --- Additional Revision Notes ---

# 1. Function without parameters:
def greet():
    print("Hello, World!")

greet()                     # Output: Hello, World!

# 2. Function with parameters:
def add(a, b):
    return a + b

result = add(5, 3)          # result = 8

# 3. Function without return value:
def greet_user(name):
    print(f"Hello, {name}!")

greet_user("Amit")          # Output: Hello, Amit!
# This function returns None by default

# 4. Function with default parameters:
def greet(name="Guest"):
    print(f"Hello, {name}!")

greet()                     # Hello, Guest!
greet("Raj")                # Hello, Raj!

def power(base, exp=2):
    return base ** exp

print(power(5))             # 25 (5 squared)
print(power(5, 3))          # 125 (5 cubed)

# 5. Function with multiple return values (using tuple):
def get_min_max(numbers):
    return min(numbers), max(numbers)

min_val, max_val = get_min_max([1, 2, 3, 4, 5])
print(min_val, max_val)     # 1 5

# 6. Keyword arguments (named arguments):
def display_info(name, age, city):
    print(f"{name} is {age} years old and lives in {city}")

display_info(age=25, city="Delhi", name="Amit")
# Order doesn't matter with keyword arguments

# 7. Arbitrary arguments (*args - tuple):
def sum_all(*args):
    total = 0
    for num in args:
        total += num
    return total

print(sum_all(1, 2, 3, 4, 5))   # 15

# 8. Arbitrary keyword arguments (**kwargs - dictionary):
def print_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_details(name="Amit", age=25, city="Delhi")
# Output:
# name: Amit
# age: 25
# city: Delhi

# 9. Function with type hints (optional):
def multiply(a: int, b: int) -> int:
    return a * b

# Type hints are just for documentation, Python doesn't enforce them

# 10. Scope of variables:

# Global variable
x = 10

def modify_global():
    global x        # Use global keyword to modify global variable
    x = 20

def local_example():
    y = 5           # Local variable (only inside function)
    return y

# print(y)          # Error! y is not defined outside function

# 11. Nested functions:
def outer_function():
    print("Outer function")
    
    def inner_function():
        print("Inner function")
    
    inner_function()    # Must be called from within outer

outer_function()
# inner_function()    # Error! Inner function not accessible outside

# 12. Lambda functions (anonymous functions):
# Single-line functions without def keyword
square = lambda x: x ** 2
print(square(5))        # 25

# Lambda with multiple arguments:
add = lambda a, b: a + b
print(add(3, 4))        # 7

# Lambda used with built-in functions:
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))    # [1, 4, 9, 16, 25]
evens = list(filter(lambda x: x % 2 == 0, numbers))  # [2, 4]

# 13. Recursive function (function calling itself):
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))     # 120

# 14. Docstrings - Documenting functions:
def divide(a, b):
    """
    Divide two numbers.
    
    Args:
        a (float): First number (dividend)
        b (float): Second number (divisor)
    
    Returns:
        float: Result of division
    
    Raises:
        ZeroDivisionError: If b is 0
    """
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

# Access docstring:
print(divide.__doc__)

# 15. Best practices:
# - Use descriptive function names (verb + noun)
# - Keep functions small and focused (single responsibility)
# - Use type hints for clarity
# - Add docstrings for complex functions
# - Avoid modifying global variables inside functions (use parameters/return)

# 16. Common mistakes:
# - Forgetting to return a value (returns None)
# - Mixing up parameter order in function calls
# - Modifying mutable arguments in place unexpectedly
# - Not handling edge cases (empty lists, zero division, etc.)

# 17. Python vs other languages:
# - No function overloading (last definition wins)
# - Functions are objects (can be passed as arguments)
# - Functions can be defined anywhere (not just at class level)