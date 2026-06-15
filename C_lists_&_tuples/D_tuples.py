# Tuples in Python

# A built-in data type that lets us create IMMUTABLE sequences of values.
# Once created, elements CANNOT be changed, added, or removed.

# Creating tuples:
tup = (87, 64, 33, 95, 76)    # Access: tup[0], tup[1], tup[2]...
# tup[0] = 43                  # NOT allowed in Python (TypeError)

# Different ways to create tuples:
tup1 = ()                      # Empty tuple
tup2 = (1, )                   # Single element tuple (comma is MUST!)
tup3 = (1, 2, 3)               # Tuple with multiple elements

# --- Additional Revision Notes ---

# 1. Why use tuples?
#    - Data integrity (cannot be accidentally modified)
#    - Faster than lists (less memory overhead)
#    - Can be used as dictionary keys (lists cannot)
#    - Safer for fixed data (days of week, months, coordinates)

# 2. Tuple without parentheses (tuple packing):
tup4 = 1, 2, 3                 # Also a valid tuple -> (1, 2, 3)

# 3. Single element tuple - IMPORTANT:
single = (5)                   # This is an INTEGER, not a tuple!
print(type(single))            # <class 'int'>
single_correct = (5,)          # This is a TUPLE
print(type(single_correct))    # <class 'tuple'>

# 4. Accessing tuple elements (same as lists):
tup = (10, 20, 30, 40, 50)
print(tup[0])      # 10
print(tup[-1])     # 50
print(tup[1:4])    # (20, 30, 40) - slicing returns a new tuple
print(tup[::-1])   # (50, 40, 30, 20, 10) - reversed

# 5. Tuple Methods (only 2 methods):
tup = (1, 2, 3, 1, 4, 1, 5)

# count() - Count occurrences of a value
print(tup.count(1))    # 3 (three occurrences of 1)

# index() - Find first occurrence index
print(tup.index(3))    # 2 (index of first 3)
print(tup.index(1))    # 0 (index of first 1)

# 6. Checking if element exists:
if 3 in tup:
    print("3 is in tuple")

# 7. Length of tuple:
print(len(tup))        # 7

# 8. Looping through tuples:
for item in tup:
    print(item)

# Using index:
for i in range(len(tup)):
    print(f"Index {i}: {tup[i]}")

# 9. Tuple concatenation and repetition:
tup_a = (1, 2, 3)
tup_b = (4, 5, 6)
combined = tup_a + tup_b    # (1, 2, 3, 4, 5, 6)
repeated = tup_a * 3        # (1, 2, 3, 1, 2, 3, 1, 2, 3)

# 10. Nested tuples:
nested = ((1, 2), (3, 4), (5, 6))
print(nested[0])      # (1, 2)
print(nested[0][1])   # 2

# 11. Converting between list and tuple:
my_list = [1, 2, 3, 4]
my_tuple = tuple(my_list)    # (1, 2, 3, 4)
back_to_list = list(my_tuple) # [1, 2, 3, 4]

# 12. Tuple unpacking:
coordinates = (10, 20)
x, y = coordinates    # x = 10, y = 20

# Swapping variables using tuple unpacking:
a = 5
b = 10
a, b = b, a           # Swaps: a = 10, b = 5

# 13. Returning multiple values from function (using tuples):
def get_min_max(numbers):
    return min(numbers), max(numbers)

result = get_min_max([1, 2, 3, 4, 5])  # (1, 5)
min_val, max_val = get_min_max([1, 2, 3, 4, 5])  # min_val=1, max_val=5

# Key Differences: List vs Tuple
# List: MUTABLE, more methods, slower, uses more memory
# Tuple: IMMUTABLE, only count() and index(), faster, uses less memory