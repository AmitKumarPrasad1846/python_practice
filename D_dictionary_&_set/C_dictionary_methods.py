# Dictionary Methods

myDict = {
    "name": "amit",
    "marks": 85,
    "roll_no": 23
}

# 1. keys() - Returns all the keys (as a view object)
myDict.keys()        # Returns: dict_keys(['name', 'marks', 'roll_no'])

# 2. values() - Returns all the values (as a view object)
myDict.values()      # Returns: dict_values(['amit', 85, 23])

# 3. items() - Returns all (key, value) pairs as tuples (as a view object)
myDict.items()       # Returns: dict_items([('name', 'amit'), ('marks', 85), ('roll_no', 23)])

# 4. get() - Returns the value for the specified key
myDict.get("name")   # Returns: "amit" (corrected: returns value according to key)
# myDict.get("key") - Safe access, returns None if key doesn't exist

# 5. update() - Inserts specified key-value pairs into the dictionary
newDict = {}
myDict.update(newDict)  # Adds items from newDict (no change since empty)
# To use correctly:
myDict.update({"city": "Delhi"})  # Adds "city": "Delhi" to myDict

# --- Additional Revision Notes ---

# 1. Using keys(), values(), items() with loops:
for key in myDict.keys():
    print(key)           # Prints: name, marks, roll_no

for value in myDict.values():
    print(value)         # Prints: amit, 85, 23

for key, value in myDict.items():
    print(f"{key}: {value}")  # Prints each key-value pair

# 2. Converting view objects to lists:
keys_list = list(myDict.keys())      # ['name', 'marks', 'roll_no']
values_list = list(myDict.values())  # ['amit', 85, 23]
items_list = list(myDict.items())    # [('name', 'amit'), ('marks', 85), ('roll_no', 23)]

# 3. get() with default value:
myDict.get("age")          # Returns: None (key doesn't exist)
myDict.get("age", 18)      # Returns: 18 (default value if key not found)

# 4. update() examples:
myDict = {"a": 1, "b": 2}
myDict.update({"b": 3, "c": 4})   # Updates 'b', adds 'c' -> {"a":1, "b":3, "c":4}

# Merging another dictionary:
new_data = {"d": 5, "e": 6}
myDict.update(new_data)           # {"a":1, "b":3, "c":4, "d":5, "e":6}

# 5. Important differences:
# - keys(), values(), items() return VIEW objects (not lists)
# - View objects are dynamic - reflect changes in dictionary
# - get() is safe - doesn't raise KeyError if key not found
# - update() modifies the original dictionary (in-place)

# 6. Other useful dictionary methods:
# pop(key) - Removes and returns value for key
myDict.pop("b")          # Removes 'b' and returns 3

# popitem() - Removes and returns last inserted item
myDict.popitem()         # Returns and removes last item

# clear() - Removes all items
myDict.clear()           # {}

# copy() - Creates a shallow copy
dict_copy = myDict.copy()

# 7. Common mistakes:
# - Forgetting to convert view objects to lists when needed
# - Using get() incorrectly (thinking it returns the key for a value)
# - Forgetting that update() modifies the original dictionary