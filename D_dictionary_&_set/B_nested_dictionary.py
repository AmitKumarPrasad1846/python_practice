# Dictionary in python
# nested dictionary

student = {
    "name" : "amit",
    "score" : {
        "chem" : 98,
        "phy" : 97,
        "math" : 95
    }
}

# Detailed version
# Nested Dictionary

# A nested dictionary is a dictionary that contains another dictionary as a value

student = {
    "name": "amit",
    "score": {
        "chem": 98,
        "phy": 97,
        "math": 95
    }
}

# Accessing nested dictionary values:
student["name"]              # Returns: "amit"
student["score"]             # Returns: {"chem": 98, "phy": 97, "math": 95}
student["score"]["chem"]     # Returns: 98
student["score"]["phy"]      # Returns: 97
student["score"]["math"]     # Returns: 95

# --- Additional Revision Notes ---

# 1. Creating nested dictionaries:
# Method 1: Direct declaration (as above)
# Method 2: Step by step
student = {}
student["name"] = "amit"
student["score"] = {}
student["score"]["chem"] = 98
student["score"]["phy"] = 97
student["score"]["math"] = 95

# 2. Accessing nested values safely (to avoid KeyError):
# Using get() for nested dictionaries
chem_marks = student.get("score", {}).get("chem")  # Returns 98
bio_marks = student.get("score", {}).get("bio")    # Returns None (key doesn't exist)

# 3. Modifying nested values:
student["score"]["chem"] = 99        # Update existing value
student["score"]["bio"] = 96         # Add new subject

# 4. Adding new nested dictionary:
student["address"] = {
    "city": "Delhi",
    "state": "Delhi",
    "country": "India"
}

# 5. Iterating through nested dictionaries:
for key, value in student.items():
    if isinstance(value, dict):      # Check if value is a dictionary
        print(f"{key}:")
        for sub_key, sub_value in value.items():
            print(f"  {sub_key}: {sub_value}")
    else:
        print(f"{key}: {value}")

# Output:
# name: amit
# score:
#   chem: 98
#   phy: 97
#   math: 95

# 6. Accessing deep nested values:
# Example with multiple levels
college = {
    "students": {
        "amit": {
            "score": {
                "chem": 98,
                "phy": 97
            }
        }
    }
}

# Accessing deep nested value:
college["students"]["amit"]["score"]["chem"]   # Returns: 98

# 7. Updating nested dictionaries:
student = {
    "name": "amit",
    "score": {"chem": 98, "phy": 97}
}

# Update specific nested value
student["score"]["chem"] = 99
# OR
student["score"].update({"chem": 99, "math": 95})

# 8. Deleting nested values:
del student["score"]["chem"]     # Removes 'chem' from score
# del student["score"]            # Removes entire score dictionary
# del student                     # Deletes entire dictionary

# 9. Checking if key exists in nested dictionary:
if "score" in student and "chem" in student["score"]:
    print(student["score"]["chem"])

# 10. Practical use case - Student records:
students = {
    "student1": {
        "name": "Amit",
        "subjects": {"math": 85, "science": 90, "english": 88},
        "grade": "A"
    },
    "student2": {
        "name": "Priya",
        "subjects": {"math": 78, "science": 85, "english": 92},
        "grade": "B"
    }
}

# Accessing student2's science marks:
students["student2"]["subjects"]["science"]   # Returns: 85

# Adding new student:
students["student3"] = {
    "name": "Raj",
    "subjects": {"math": 95, "science": 93, "english": 90},
    "grade": "A+"
}

# 11. Finding average of all students:
total_math = 0
count = 0
for student in students.values():
    total_math += student["subjects"]["math"]
    count += 1
avg_math = total_math / count   # Average math score

# 12. Dictionary comprehension with nested dictionaries:
# Creating nested dictionary
squares = {x: {"square": x**2, "cube": x**3} for x in range(3)}
# {0: {'square': 0, 'cube': 0}, 1: {'square': 1, 'cube': 1}, 2: {'square': 4, 'cube': 8}}

# Key Points to Remember:
# - Nested dictionaries allow organizing complex, hierarchical data
# - Access using chain of keys: dict[key1][key2][key3]...
# - Always use get() or check existence to avoid KeyError
# - Use isinstance(value, dict) to check if value is a dictionary
# - Nested dictionaries are mutable (can be modified, added, deleted)