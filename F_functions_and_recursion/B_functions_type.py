# Functions in Python

# Two types of functions:
# 1. Built-in Functions
# 2. User-defined Functions

# Examples of Built-in Functions:
print()
len()
type()
range()

# --- Additional Revision Notes ---

# 1. Built-in Functions - Overview:
# Python comes with many built-in functions that are always available

# Common Built-in Functions:

# a) print() - Display output
print("Hello, World!")

# b) len() - Get length of sequence
print(len("Python"))        # 6
print(len([1, 2, 3, 4]))    # 4

# c) type() - Get type of object
print(type(5))              # <class 'int'>
print(type("Hello"))        # <class 'str'>
print(type([1, 2, 3]))      # <class 'list'>

# d) range() - Generate sequence of numbers
for i in range(5):
    print(i)                # 0, 1, 2, 3, 4

# 2. Other Important Built-in Functions:

# a) input() - Take user input
name = input("Enter your name: ")
print(f"Hello, {name}!")

# b) int(), float(), str() - Type conversion
num = int("10")             # 10 (string to int)
pi = float("3.14")          # 3.14 (string to float)
text = str(123)             # "123" (int to string)

# c) min(), max() - Find min/max value
numbers = [10, 5, 8, 3, 12]
print(min(numbers))         # 3
print(max(numbers))         # 12

# d) sum() - Sum of all elements
print(sum(numbers))         # 38

# e) sorted() - Return sorted list
sorted_nums = sorted(numbers)   # [3, 5, 8, 10, 12]
sorted_desc = sorted(numbers, reverse=True)  # [12, 10, 8, 5, 3]

# f) abs() - Absolute value
print(abs(-5))              # 5

# g) pow() - Power of a number
print(pow(2, 3))            # 8 (2^3)

# h) round() - Round decimal number
print(round(3.14159, 2))    # 3.14

# i) eval() - Evaluate string as Python expression
result = eval("2 + 3 * 4")  # 14

# j) id() - Unique identifier of object
x = 5
print(id(x))                # Memory address of x

# k) help() - Get help/documentation
help(print)                 # Shows documentation for print()

# l) dir() - List attributes/methods of object
print(dir(list))            # Shows list methods

# 3. Type Conversion Functions:
# int() - Convert to integer
# float() - Convert to float
# str() - Convert to string
# bool() - Convert to boolean
# list() - Convert to list
# tuple() - Convert to tuple
# set() - Convert to set
# dict() - Convert to dictionary

print(int(3.14))            # 3
print(float(5))             # 5.0
print(bool(0))              # False
print(bool(5))              # True
print(list("hello"))        # ['h', 'e', 'l', 'l', 'o']
print(tuple([1, 2, 3]))     # (1, 2, 3)

# 4. String Built-in Functions:
text = "Hello World"
print(len(text))            # 11
print(text.upper())         # "HELLO WORLD"
print(text.lower())         # "hello world"
print(text.count("l"))      # 3
print(text.find("World"))   # 6
print(text.replace("World", "Python"))  # "Hello Python"

# 5. Collection Built-in Functions:
my_list = [1, 2, 3, 4, 5]

# any() - True if any element is True
print(any([0, 1, 0]))       # True

# all() - True if all elements are True
print(all([1, 2, 3]))       # True
print(all([1, 0, 3]))       # False

# enumerate() - Get index-value pairs
for idx, val in enumerate(my_list):
    print(f"Index {idx}: {val}")

# zip() - Combine multiple iterables
names = ["Amit", "Priya", "Raj"]
marks = [85, 92, 78]
for name, mark in zip(names, marks):
    print(f"{name}: {mark}")

# filter() - Filter elements
evens = list(filter(lambda x: x % 2 == 0, my_list))
print(evens)                # [2, 4]

# map() - Apply function to all elements
squares = list(map(lambda x: x**2, my_list))
print(squares)              # [1, 4, 9, 16, 25]

# 6. Input/Output Functions:
# input() - Get input from user
# print() - Display output (with separators)
print("Hello", "World", sep="-", end="!")
# Output: Hello-World!

# 7. Math Functions (from math module):
import math
print(math.sqrt(16))        # 4.0
print(math.ceil(3.14))      # 4
print(math.floor(3.14))     # 3
print(math.pi)              # 3.141592653589793

# 8. Most Commonly Used Built-in Functions:
"""
print()      - Display output
len()        - Get length
type()       - Get type
input()      - Get user input
int()        - Convert to integer
str()        - Convert to string
float()      - Convert to float
list()       - Convert to list
tuple()      - Convert to tuple
dict()       - Convert to dictionary
set()        - Convert to set
range()      - Generate range
sum()        - Sum of elements
min()        - Minimum value
max()        - Maximum value
sorted()     - Sort elements
abs()        - Absolute value
pow()        - Power function
round()      - Round numbers
enumerate()  - Get index-value pairs
zip()        - Combine iterables
help()       - Get documentation
dir()        - List attributes
"""

# 9. Finding available built-in functions:
import builtins
print(dir(builtins))        # Shows all built-in names

# 10. Difference between Built-in and User-defined:
# Built-in: Already available, imported by default
# User-defined: Created by programmer using 'def' keyword

# User-defined function example:
def custom_add(a, b):
    return a + b

print(custom_add(3, 4))     # 7 (User-defined)
print(sum([3, 4]))          # 7 (Built-in)