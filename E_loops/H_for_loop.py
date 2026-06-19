# Loops in Python

# Loops are used for sequential traversal.
# For traversing list, string, tuples, etc.

# for Loops

# Basic syntax:
list = [1, 2, 3]
for el in list:
    print(el)           # Prints each element
# Output: 1, 2, 3

# for Loop with else:
for el in list:
    print(el)
else:
    print("END")        # Executes when loop completes normally

# --- Additional Revision Notes ---

# 1. for loop with different data types:

# a) List
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# b) String
word = "Python"
for char in word:
    print(char)         # Prints P, y, t, h, o, n

# c) Tuple
colors = ("red", "green", "blue")
for color in colors:
    print(color)

# d) Dictionary
student = {"name": "Amit", "age": 20, "city": "Delhi"}
for key in student:
    print(key, ":", student[key])    # Prints all key-value pairs

# e) Set
nums = {1, 2, 3, 4, 5}
for num in nums:
    print(num)          # Order may vary (unordered)

# 2. range() function with for loop:
# range(start, stop, step)

# Print 0 to 4:
for i in range(5):
    print(i)            # 0, 1, 2, 3, 4

# Print 1 to 5:
for i in range(1, 6):
    print(i)            # 1, 2, 3, 4, 5

# Print even numbers from 2 to 10:
for i in range(2, 11, 2):
    print(i)            # 2, 4, 6, 8, 10

# Print in reverse:
for i in range(5, 0, -1):
    print(i)            # 5, 4, 3, 2, 1

# 3. Nested for loops:
for i in range(3):
    for j in range(3):
        print(f"i={i}, j={j}")

# 4. for loop with break:
for i in range(1, 6):
    if i == 3:
        break           # Stops when i is 3
    print(i)
# Output: 1, 2

# 5. for loop with continue:
for i in range(1, 6):
    if i == 3:
        continue        # Skips 3
    print(i)
# Output: 1, 2, 4, 5

# 6. for loop with else (important):
# else executes ONLY if loop completes without break

for i in range(1, 6):
    if i == 10:         # This condition never true
        break
    print(i)
else:
    print("Loop completed successfully")
# Output: 1, 2, 3, 4, 5, "Loop completed successfully"

# With break (else won't execute):
for i in range(1, 6):
    if i == 3:
        break
    print(i)
else:
    print("Loop completed successfully")  # This won't execute
# Output: 1, 2

# 7. enumerate() - Get both index and value:
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
# Output:
# 0: apple
# 1: banana
# 2: cherry

# 8. zip() - Iterate multiple lists simultaneously:
names = ["Amit", "Priya", "Raj"]
marks = [85, 92, 78]
for name, mark in zip(names, marks):
    print(f"{name} scored {mark} marks")

# 9. List comprehension (compact for loop):
squares = [x**2 for x in range(5)]          # [0, 1, 4, 9, 16]
evens = [x for x in range(10) if x % 2 == 0] # [0, 2, 4, 6, 8]

# 10. Practical examples:

# a) Find sum of all elements:
numbers = [10, 20, 30, 40, 50]
total = 0
for num in numbers:
    total += num
print(f"Sum: {total}")      # 150

# b) Find max element:
numbers = [10, 25, 5, 40, 15]
max_num = numbers[0]
for num in numbers:
    if num > max_num:
        max_num = num
print(f"Maximum: {max_num}")  # 40

# c) Check if element exists:
numbers = [2, 4, 6, 8, 10]
target = 6
found = False
for num in numbers:
    if num == target:
        found = True
        break
print(f"Found: {found}")    # True

# 11. for loop with dictionaries - different ways:
student = {"name": "Amit", "age": 20, "city": "Delhi"}

# Through keys:
for key in student:
    print(key, ":", student[key])

# Through values:
for value in student.values():
    print(value)

# Through items (key-value pairs):
for key, value in student.items():
    print(key, ":", value)

# 12. Important notes:
# - for loop is used when number of iterations is KNOWN
# - while loop is used when number of iterations is UNKNOWN
# - range() is commonly used with for loops
# - else with for executes only if loop completes without break
# - for loops can iterate over ANY iterable objects