# range()

# Range function returns a sequence of numbers, starting from 0 by default,
# and increments by 1 (by default), and stops before a specified number.

# Syntax: range(start?, stop, step?)

# Examples:
for el in range(5):
    print(el)
# Output: 0, 1, 2, 3, 4

for el in range(1, 5):
    print(el)
# Output: 1, 2, 3, 4

for el in range(1, 5, 2):
    print(el)
# Output: 1, 3

# --- Additional Revision Notes ---

# 1. range() with one argument (start=0, step=1):
for i in range(5):
    print(i)        # 0, 1, 2, 3, 4

# 2. range() with two arguments (start, stop, step=1):
for i in range(2, 7):
    print(i)        # 2, 3, 4, 5, 6

# 3. range() with three arguments (start, stop, step):
for i in range(1, 10, 2):
    print(i)        # 1, 3, 5, 7, 9

for i in range(2, 11, 2):
    print(i)        # 2, 4, 6, 8, 10

# 4. range() with negative step (reverse order):
for i in range(5, 0, -1):
    print(i)        # 5, 4, 3, 2, 1

for i in range(10, 0, -2):
    print(i)        # 10, 8, 6, 4, 2

# 5. Converting range to list/tuple:
nums_list = list(range(5))      # [0, 1, 2, 3, 4]
nums_tuple = tuple(range(5))    # (0, 1, 2, 3, 4)
nums_set = set(range(5))        # {0, 1, 2, 3, 4}

# 6. range() with negative numbers:
for i in range(-5, 0):
    print(i)        # -5, -4, -3, -2, -1

for i in range(-10, -1, 2):
    print(i)        # -10, -8, -6, -4, -2

# 7. Important characteristics:
# - range() creates a RANGE OBJECT (not a list) - memory efficient
# - It generates values on the fly (lazy evaluation)
# - The stop value is EXCLUDED (stops before stop)
# - All arguments must be integers

# 8. Checking if value exists in range:
if 5 in range(10):
    print("5 is in range")   # True

if 10 in range(5):
    print("10 is in range")  # False

# 9. len() with range:
print(len(range(10)))       # 10
print(len(range(2, 10, 2))) # 4 (2,4,6,8)

# 10. Common use cases:

# a) Print table of a number:
num = 5
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

# b) Sum of first n natural numbers:
n = 10
total = 0
for i in range(1, n+1):
    total += i
print(f"Sum: {total}")       # 55

# c) Find factorial:
n = 5
fact = 1
for i in range(1, n+1):
    fact *= i
print(f"Factorial: {fact}")  # 120

# d) Pattern printing:
for i in range(1, 6):
    print("*" * i)
# Output:
# *
# **
# ***
# ****
# *****

# 11. range() vs list comparison:
# range object uses less memory:
import sys
range_obj = range(1000000)
list_obj = list(range(1000000))
print(sys.getsizeof(range_obj))  # ~48 bytes (small)
print(sys.getsizeof(list_obj))   # ~8 MB (large)

# 12. Nested range loops:
for i in range(3):
    for j in range(3):
        print(f"({i}, {j})")
# Output: (0,0), (0,1), (0,2), (1,0), (1,1), (1,2), (2,0), (2,1), (2,2)

# 13. range() with enumerate:
fruits = ["apple", "banana", "cherry"]
for idx, fruit in enumerate(fruits):
    print(f"Index {idx}: {fruit}")
# Instead of:
# for idx in range(len(fruits)):
#     print(f"Index {idx}: {fruits[idx]}")

# Key Points:
# - range(start, stop, step)
# - start is optional (default: 0)
# - stop is MANDATORY (excluded)
# - step is optional (default: 1)
# - All arguments must be integers
# - Memory efficient (generates values on demand)