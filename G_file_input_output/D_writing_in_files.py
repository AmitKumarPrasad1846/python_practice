# ========================================
# WRITING TO FILES IN PYTHON
# ========================================

# Two main modes for writing:
# 'w' - Write mode (overwrites entire file)
# 'a' - Append mode (adds to end of file)

# ========================================
# METHOD 1: WRITE MODE ('w') - OVERWRITES
# ========================================

# Creates new file or overwrites existing content
f = open("demo.txt", "w")
f.write("this is a new line")    # Overwrites entire file
f.close()

# Better way using 'with' (auto-closes)
with open("demo.txt", "w") as f:
    f.write("this is a new line")    # Overwrites everything

# Writing multiple lines
with open("demo.txt", "w") as f:
    f.write("First line\n")
    f.write("Second line\n")
    f.write("Third line")

# ========================================
# METHOD 2: APPEND MODE ('a') - ADDS TO END
# ========================================

# Adds content to the end of file without deleting existing content
f = open("demo.txt", "a")
f.write("this is a new line")    # Adds to end of file
f.close()

# Better way using 'with'
with open("demo.txt", "a") as f:
    f.write("this is a new line\n")    # Adds to end

# ========================================
# WRITING MULTIPLE LINES
# ========================================

# Method 1: Multiple write() calls
with open("demo.txt", "w") as f:
    f.write("Line 1\n")
    f.write("Line 2\n")
    f.write("Line 3\n")

# Method 2: writelines() - Writes a list of strings
lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
with open("demo.txt", "w") as f:
    f.writelines(lines)

# Method 3: Using join()
lines = ["Line 1", "Line 2", "Line 3"]
with open("demo.txt", "w") as f:
    f.write("\n".join(lines))    # Joins with newline

# ========================================
# 'w' vs 'a' - IMPORTANT DIFFERENCE
# ========================================

# WRITE MODE ('w') - OVERWRITES EVERYTHING
with open("demo.txt", "w") as f:
    f.write("New content")    # File now has ONLY "New content"

# APPEND MODE ('a') - ADDS TO END
with open("demo.txt", "a") as f:
    f.write("Added content")   # File now has "New contentAdded content"

# ========================================
# OTHER WRITING MODES
# ========================================

# 'x' - Exclusive creation (fails if file exists)
try:
    with open("new_file.txt", "x") as f:
        f.write("This file is new")
except FileExistsError:
    print("File already exists!")

# 'r+' - Read and Write (file must exist)
with open("demo.txt", "r+") as f:
    content = f.read()         # Read existing content
    f.write("Added in r+ mode") # Write to file

# 'w+' - Write and Read (creates/overwrites)
with open("demo.txt", "w+") as f:
    f.write("New content")
    f.seek(0)                  # Go to beginning
    content = f.read()         # Read what was written

# 'a+' - Append and Read
with open("demo.txt", "a+") as f:
    f.write("Added content")
    f.seek(0)                  # Go to beginning
    content = f.read()         # Read entire file

# ========================================
# WRITING BINARY FILES
# ========================================

# 'wb' - Write binary
data = b"Binary data here"
with open("output.bin", "wb") as f:
    f.write(data)

# ========================================
# PRACTICAL EXAMPLES
# ========================================

# 1. Create a new file with content
with open("new_file.txt", "w") as f:
    f.write("Hello, World!\n")
    f.write("This is a new file.")

# 2. Add to existing file
with open("existing_file.txt", "a") as f:
    f.write("This line is appended\n")

# 3. Write a list to file
fruits = ["apple", "banana", "cherry", "date"]
with open("fruits.txt", "w") as f:
    for fruit in fruits:
        f.write(fruit + "\n")

# 4. Write dictionary to file
student = {"name": "Amit", "age": 20, "city": "Delhi"}
with open("student.txt", "w") as f:
    for key, value in student.items():
        f.write(f"{key}: {value}\n")

# 5. Write numbers 1 to 10
with open("numbers.txt", "w") as f:
    for i in range(1, 11):
        f.write(str(i) + "\n")

# 6. Create CSV file
import csv
with open("data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Age", "City"])
    writer.writerow(["Amit", 25, "Delhi"])
    writer.writerow(["Priya", 22, "Mumbai"])

# 7. Write JSON file
import json
data = {"name": "Amit", "age": 25, "city": "Delhi"}
with open("data.json", "w") as f:
    json.dump(data, f, indent=4)    # indent for pretty formatting

# 8. Write to file with formatting
name = "Raj"
score = 95
with open("scores.txt", "w") as f:
    f.write(f"Name: {name}\n")
    f.write(f"Score: {score}\n")

# ========================================
# WRITING VS APPENDING - QUICK REFERENCE
# ========================================

# 'w' - OVERWRITE:
# - Creates file if doesn't exist
# - Deletes all existing content
# - Writes new content
# - Use when you want to start fresh

# 'a' - APPEND:
# - Creates file if doesn't exist
# - Keeps existing content
# - Adds new content at the end
# - Use when you want to add to existing content

# ========================================
# IMPORTANT NOTES
# ========================================

# 1. 'w' creates file if it doesn't exist
# 2. 'w' deletes everything in file before writing
# 3. 'a' creates file if it doesn't exist
# 4. 'a' keeps existing content and adds at end
# 5. Always add newline '\n' to separate lines
# 6. Use 'with' statement for automatic closing
# 7. write() expects a string, not numbers
# 8. Convert numbers to string: str(5) or f"{5}"

# ========================================
# COMMON MISTAKES
# ========================================

# Mistake 1: Forgetting newline character
with open("file.txt", "w") as f:
    f.write("Line 1")
    f.write("Line 2")    # Results in "Line 1Line 2"

# Correct:
with open("file.txt", "w") as f:
    f.write("Line 1\n")
    f.write("Line 2\n")

# Mistake 2: Using 'w' instead of 'a' (accidentally deleting content)
# Mistake 3: Forgetting to convert numbers to strings
# Mistake 4: Not using 'with' and forgetting to close

# ========================================
# QUICK REFERENCE
# ========================================

# f.write("text")       -> Write string to file
# f.writelines(list)    -> Write list of strings
# 'w' mode              -> Overwrite entire file
# 'a' mode              -> Append to end of file
# 'x' mode              -> Create new file (fail if exists)
# 'rb'/'wb'             -> Read/Write binary files