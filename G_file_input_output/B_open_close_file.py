# 1. Opening a File:
# Syntax: open(file_name, mode)
# file_name: Name/path of the file
# mode: How you want to open the file

# Common modes:
# 'r'  - Read (default) - Open file for reading
# 'w'  - Write - Open file for writing (overwrites existing content)
# 'a'  - Append - Open file for writing (adds to end of file)
# 'x'  - Exclusive creation - Creates new file, fails if exists
# 't'  - Text mode (default) - Opens file in text mode
# 'b'  - Binary mode - Opens file in binary mode
# '+'  - Read and Write - Opens file for both reading and writing

# 2. Opening Text Files:
# Open for reading (default mode)
file = open("example.txt", "r")

# Open for writing (creates new file or overwrites)
file = open("example.txt", "w")

# Open for appending (adds to end of file)
file = open("example.txt", "a")

# Open for reading and writing
file = open("example.txt", "r+")

# 3. Opening Binary Files:
# Open binary file for reading
file = open("image.png", "rb")

# Open binary file for writing
file = open("image.png", "wb")

# 4. Reading from Text Files:
file = open("example.txt", "r")

# read() - Reads entire file
content = file.read()
print(content)

# readline() - Reads one line
line = file.readline()
print(line)

# readlines() - Reads all lines into a list
lines = file.readlines()
print(lines)  # ['Line 1\n', 'Line 2\n', 'Line 3']

# Looping through lines
for line in file:
    print(line)

# 5. Writing to Text Files:
file = open("example.txt", "w")

# write() - Writes a string
file.write("Hello, World!\n")
file.write("This is line 2\n")

# writelines() - Writes a list of strings
lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
file.writelines(lines)

# 6. Appending to Text Files:
file = open("example.txt", "a")
file.write("This will be added at the end\n")
file.close()

# 7. Closing a File (VERY IMPORTANT!):
file = open("example.txt", "r")
# ... do operations ...
file.close()  # Always close the file to free resources

# 8. Using 'with' statement (BEST PRACTICE):
# Automatically closes the file
with open("example.txt", "r") as file:
    content = file.read()
    print(content)
# File is automatically closed here

# 9. File Paths:
# Relative path (file in same folder)
open("data.txt")

# Relative path (file in subfolder)
open("folder/data.txt")

# Absolute path (full path)
open("C:/Users/username/Documents/data.txt")

# 10. Checking if file exists:
import os

if os.path.exists("example.txt"):
    print("File exists")
else:
    print("File does not exist")

# 11. Getting file information:
import os

# Get file size
size = os.path.getsize("example.txt")
print(f"File size: {size} bytes")

# Get file modification time
import datetime
mod_time = os.path.getmtime("example.txt")
print(f"Modified: {datetime.datetime.fromtimestamp(mod_time)}")

# 12. Reading Binary Files:
with open("image.jpg", "rb") as file:
    data = file.read()  # Returns bytes
    print(f"File size: {len(data)} bytes")

# 13. Writing Binary Files:
data = b"Binary data"
with open("output.bin", "wb") as file:
    file.write(data)

# 14. Common File Operations:

# a) Copy a file:
with open("source.txt", "r") as source:
    content = source.read()
with open("destination.txt", "w") as dest:
    dest.write(content)

# b) Count lines in a file:
with open("example.txt", "r") as file:
    line_count = sum(1 for line in file)
print(f"Lines: {line_count}")

# c) Search for a word:
with open("example.txt", "r") as file:
    for line in file:
        if "search_word" in line:
            print("Found in:", line)

# 15. Working with CSV files:
import csv

# Writing CSV
with open("data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age", "City"])
    writer.writerow(["Amit", 25, "Delhi"])
    writer.writerow(["Priya", 22, "Mumbai"])

# Reading CSV
with open("data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# 16. Working with JSON files:
import json

# Writing JSON
data = {"name": "Amit", "age": 25, "city": "Delhi"}
with open("data.json", "w") as file:
    json.dump(data, file)

# Reading JSON
with open("data.json", "r") as file:
    data = json.load(file)
    print(data["name"])  # Amit

# 17. Exception Handling with Files:
try:
    with open("nonexistent.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("File not found!")
except PermissionError:
    print("Permission denied!")
except Exception as e:
    print(f"An error occurred: {e}")

# 18. File Modes Summary:

# Mode | Description
# -----|-----------
# 'r'  | Read (default) - file must exist
# 'w'  | Write - creates new file or overwrites
# 'a'  | Append - creates new file or appends
# 'x'  | Exclusive creation - creates new file, fails if exists
# 'r+' | Read and Write - file must exist
# 'w+' | Write and Read - creates new file or overwrites
# 'a+' | Append and Read - creates new file or appends
# 'rb' | Read Binary
# 'wb' | Write Binary
# 'ab' | Append Binary

# 19. Important Points:
# - Always close files (using close() or with statement)
# - Use 'with' statement for automatic closing
# - Handle exceptions when working with files
# - Check if file exists before reading
# - Use appropriate mode for your operation
# - Text vs Binary mode matters for different file types

# 20. Best Practices:
# 1. Use 'with' statement for automatic file closing
# 2. Handle exceptions properly
# 3. Use appropriate modes (r, w, a, rb, wb)
# 4. Close files when done (if not using 'with')
# 5. Use try-except for file operations
# 6. Use os.path methods to check file existence
# 7. Be careful with file paths (use relative paths when possible)