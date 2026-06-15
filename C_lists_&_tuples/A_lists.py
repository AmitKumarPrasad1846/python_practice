# Lists in Python

# A built-in data type that stores a set of values

# It can store elements of different types (integer, float, string, etc.)

marks = [87, 64, 33, 95, 76]
# Accessing: marks[0], marks[1], marks[2], marks[3], marks[4]

student = ["Karan", 85, "Delhi"]
# student[0] -> "Karan"
# student[1] -> 85
# student[2] -> "Delhi"

# Lists are MUTABLE (can be changed)
student[0] = "Arjun"   # Allowed in Python (unlike strings)
# Now student becomes: ["Arjun", 85, "Delhi"]

# len() returns the length of the list
len(student)   # Returns: 3
len(marks)     # Returns: 5

# --- Additional Revision Notes ---

# 1. Creating Lists:
empty_list = []
numbers = [1, 2, 3, 4, 5]
mixed = [10, "Hello", 3.14, True]
nested = [[1, 2], [3, 4], [5, 6]]  # List of lists

# 2. List Indexing (same as strings):
# Positive indexing: 0, 1, 2, ...
# Negative indexing: -1 (last), -2 (second last), ...

fruits = ["apple", "banana", "cherry", "date"]
print(fruits[0])     # apple
print(fruits[-1])    # date
print(fruits[-2])    # cherry

# 3. List Slicing (returns a new list):
print(fruits[1:3])   # ['banana', 'cherry']
print(fruits[:2])    # ['apple', 'banana']
print(fruits[2:])    # ['cherry', 'date']
print(fruits[::-1])  # Reversed: ['date', 'cherry', 'banana', 'apple']

# 4. List Methods (Common operations):

# append() - Add element at the end
fruits.append("elderberry")   # ['apple', 'banana', 'cherry', 'date', 'elderberry']

# insert() - Insert at specific index
fruits.insert(1, "blueberry")  # ['apple', 'blueberry', 'banana', 'cherry', 'date', 'elderberry']

# remove() - Remove first occurrence of value
fruits.remove("banana")        # Removes 'banana'

# pop() - Remove element at index (or last if no index)
fruits.pop()    # Removes last element
fruits.pop(0)   # Removes first element

# sort() - Sort the list (in place)
numbers = [3, 1, 4, 1, 5, 9]
numbers.sort()            # [1, 1, 3, 4, 5, 9]
numbers.sort(reverse=True) # [9, 5, 4, 3, 1, 1]

# reverse() - Reverse the list (in place)
fruits.reverse()

# index() - Find index of first occurrence
print(fruits.index("cherry"))  # Returns index

# count() - Count occurrences
print(fruits.count("apple"))

# copy() - Create a shallow copy
new_list = fruits.copy()

# extend() - Add all elements of another list
fruits.extend(["grape", "kiwi"])

# clear() - Remove all elements
fruits.clear()   # []

# 5. List Operations:
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list1 + list2      # [1, 2, 3, 4, 5, 6] (concatenation)
repeated = list1 * 3          # [1, 2, 3, 1, 2, 3, 1, 2, 3] (repetition)

# 6. Checking if element exists:
if "apple" in fruits:
    print("Apple is in the list")

# 7. Looping through lists:
for fruit in fruits:
    print(fruit)

# Using index:
for i in range(len(fruits)):
    print(f"{i}: {fruits[i]}")

# Using enumerate:
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")

# 8. List Comprehension (advanced but useful):
squares = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]
evens = [x for x in range(10) if x % 2 == 0]  # [0, 2, 4, 6, 8]


# Key Difference between Strings and Lists:
# Strings: IMMUTABLE (cannot change individual characters)
# Lists: MUTABLE (can change, add, remove elements)