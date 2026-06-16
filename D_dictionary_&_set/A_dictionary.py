# Dictionary in Python

# Dictionaries are used to store data values in key:value pairs
# They are unordered, mutable (changeable), and don't allow duplicate keys

# Syntax:
dict = {
    "name": "shradha",
    "cgpa": 9.6,
    "marks": [98, 97, 95],
}

# Format: "key": value

# Accessing values:
dict["name"]    # Returns: "shradha"
dict["cgpa"]    # Returns: 9.6
dict["marks"]   # Returns: [98, 97, 95]

# Adding or updating values:
dict["key"] = "value"   # Assigns new key-value pair or updates existing key

# --- Additional Revision Notes ---

# 1. Creating Dictionaries:
empty_dict = {}                     # Empty dictionary
dict1 = {"a": 1, "b": 2, "c": 3}    # String keys
dict2 = {1: "one", 2: "two"}        # Integer keys
dict3 = dict(name="John", age=25)   # Using dict() constructor

# 2. Dictionary Properties:
# - Keys must be IMMUTABLE (strings, numbers, tuples) - cannot use lists as keys
# - Values can be ANY data type (mutable allowed)
# - Keys are unique (if duplicate key is added, last value overwrites)
# - Dictionaries are ORDERED from Python 3.7+ (maintain insertion order)

# 3. Accessing values safely:
student = {"name": "Karan", "age": 20}

# Method 1: Direct access (raises KeyError if key doesn't exist)
print(student["name"])      # "Karan"
# print(student["city"])    # KeyError!

# Method 2: Using get() (returns None if key doesn't exist)
print(student.get("city"))   # None
print(student.get("city", "Not Found"))  # "Not Found" (custom default)

# Method 3: Using setdefault() (returns value if exists, else sets new value)
city = student.setdefault("city", "Delhi")  # Sets "city":"Delhi" and returns "Delhi"

# 4. Adding/Updating elements:
student["age"] = 21         # Update existing key
student["grade"] = "A"      # Add new key-value pair

# 5. Removing elements:
student = {"a": 1, "b": 2, "c": 3, "d": 4}

# pop() - Removes key and returns value
value = student.pop("b")    # Returns 2, student becomes {"a":1, "c":3, "d":4}

# popitem() - Removes and returns last inserted item (key, value)
item = student.popitem()    # Returns ("d", 4) (Python 3.7+)

# del - Deletes key or entire dictionary
del student["a"]            # Removes key "a"
# del student               # Deletes entire dictionary

# clear() - Removes all items
student.clear()             # Becomes {}

# 6. Dictionary Methods:

student = {"name": "Priya", "age": 22, "city": "Mumbai"}

# keys() - Returns all keys (view object)
keys = student.keys()       # dict_keys(['name', 'age', 'city'])
for key in student.keys():
    print(key)

# values() - Returns all values
values = student.values()   # dict_values(['Priya', 22, 'Mumbai'])

# items() - Returns all key-value pairs as tuples
items = student.items()     # dict_items([('name','Priya'), ('age',22), ('city','Mumbai')])
for key, value in student.items():
    print(f"{key}: {value}")

# update() - Merges another dictionary
new_data = {"age": 23, "country": "India"}
student.update(new_data)    # Updates age, adds country

# copy() - Creates a shallow copy
student_copy = student.copy()

# 7. Checking if key exists:
if "name" in student:
    print("Name exists")

if "age" in student.keys():     # Same as above
    print("Age exists")

# 8. Length of dictionary:
print(len(student))     # Number of key-value pairs

# 9. Looping through dictionaries:
# Through keys
for key in student:
    print(f"{key}: {student[key]}")

# Through items
for key, value in student.items():
    print(key, value)

# 10. Nested Dictionaries:
students = {
    "student1": {"name": "Raj", "marks": 85},
    "student2": {"name": "Simran", "marks": 92},
    "student3": {"name": "Amit", "marks": 78}
}
print(students["student2"]["name"])    # "Simran"
print(students["student3"]["marks"])   # 78

# 11. Dictionary Comprehension:
squares = {x: x**2 for x in range(5)}   # {0:0, 1:1, 2:4, 3:9, 4:16}

# 12. Merging dictionaries (Python 3.9+):
dict_a = {"a": 1, "b": 2}
dict_b = {"c": 3, "d": 4}
merged = dict_a | dict_b    # {'a':1, 'b':2, 'c':3, 'd':4}

# 13. Practical Example - Counting frequencies:
text = "hello world"
freq = {}
for char in text:
    freq[char] = freq.get(char, 0) + 1
print(freq)   # {'h':1, 'e':1, 'l':3, 'o':2, ' ':1, 'w':1, 'r':1, 'd':1}

# Key Points to Remember:
# - Dictionaries are MUTABLE
# - Keys must be UNIQUE and IMMUTABLE
# - Values can be any type (including lists, dicts, etc.)
# - Access non-existent key with [] raises KeyError
# - Use get() for safe access
# - Ordered from Python 3.7+ (maintain insertion order)