# ========================================
# READING FILES IN PYTHON
# ========================================

# OPENING A FILE
# Syntax: open("filename", "mode")
# Common modes: 'r' (read), 'w' (write), 'a' (append)

# ========================================
# METHOD 1: read() - Reads ENTIRE file
# ========================================

# Reads the whole file as a single string
with open("example.txt", "r") as f:
    content = f.read()
    print(content)

# Read specific number of characters
with open("example.txt", "r") as f:
    first_10 = f.read(10)      # Reads first 10 characters
    remaining = f.read()       # Reads rest of the file

# ========================================
# METHOD 2: readline() - Reads ONE line
# ========================================

# Reads one line at a time (includes newline character)
with open("example.txt", "r") as f:
    line1 = f.readline()       # First line
    line2 = f.readline()       # Second line
    line3 = f.readline()       # Third line

# Using readline() in a loop
with open("example.txt", "r") as f:
    line = f.readline()
    while line != "":          # Keep reading until end of file
        print(line, end="")    # end="" to avoid double newline
        line = f.readline()

# ========================================
# METHOD 3: readlines() - Reads ALL lines into a LIST
# ========================================

# Returns a list where each element is a line
with open("example.txt", "r") as f:
    lines = f.readlines()
    print(lines)               # ['Line 1\n', 'Line 2\n', 'Line 3\n']
    
    # Access specific line
    print(lines[0])            # First line
    print(lines[1])            # Second line

# ========================================
# METHOD 4: FOR LOOP - BEST for large files
# ========================================

# Most memory-efficient way to read large files
with open("example.txt", "r") as f:
    for line in f:
        print(line, end="")

# ========================================
# WORKING WITH FILE POSITION
# ========================================

# tell() - Get current position
# seek() - Move to specific position

with open("example.txt", "r") as f:
    print(f.tell())            # 0 (beginning)
    data = f.read(5)           # Read first 5 characters
    print(f.tell())            # 5 (position after reading)
    f.seek(0)                  # Go back to beginning
    data = f.read()            # Read entire file again

# ========================================
# HANDLING FILE ERRORS
# ========================================

try:
    with open("nonexistent.txt", "r") as f:
        content = f.read()
except FileNotFoundError:
    print("File not found!")
except PermissionError:
    print("Permission denied!")
except Exception as e:
    print(f"Error: {e}")

# ========================================
# CHECKING IF FILE EXISTS
# ========================================

import os

if os.path.exists("example.txt"):
    with open("example.txt", "r") as f:
        content = f.read()
else:
    print("File does not exist")

# Check if file is empty
if os.path.exists("example.txt") and os.path.getsize("example.txt") == 0:
    print("File is empty")

# ========================================
# READING LARGE FILES - COMPARISON
# ========================================

# BAD for large files (loads everything into memory)
with open("large_file.txt", "r") as f:
    content = f.read()         # Memory heavy

# GOOD for large files (processes line by line)
with open("large_file.txt", "r") as f:
    for line in f:             # Memory efficient
        process(line)

# ========================================
# PRACTICAL EXAMPLES
# ========================================

# 1. Count lines in a file
with open("example.txt", "r") as f:
    line_count = sum(1 for line in f)
    print(f"Total lines: {line_count}")

# 2. Read first N lines
n = 5
with open("example.txt", "r") as f:
    first_n = [next(f) for _ in range(n)]
    print(first_n)

# 3. Read last N lines
from collections import deque
with open("example.txt", "r") as f:
    last_5 = deque(f, 5)
    print(last_5)

# 4. Remove newline characters while reading
with open("example.txt", "r") as f:
    lines = [line.strip() for line in f]
    print(lines)               # No '\n' characters

# 5. Search for a word in file
with open("example.txt", "r") as f:
    for line in f:
        if "search_word" in line:
            print("Found:", line)

# ========================================
# READING BINARY FILES
# ========================================

# Read image/audio/video files
with open("image.jpg", "rb") as f:    # 'rb' = read binary
    data = f.read()                    # Returns bytes
    print(f"File size: {len(data)} bytes")

# ========================================
# DIFFERENT FILE PATHS
# ========================================

# Same folder
open("file.txt")

# Subfolder
open("folder/file.txt")

# Absolute path (Windows)
open("C:/Users/User/Documents/file.txt")

# Absolute path (Mac/Linux)
open("/home/user/Documents/file.txt")

# ========================================
# QUICK REFERENCE
# ========================================

# f.read()          -> Read entire file (string)
# f.readline()      -> Read one line (string)
# f.readlines()     -> Read all lines (list)
# for line in f:    -> Loop through lines (memory efficient)
# f.tell()          -> Get current position
# f.seek(0)         -> Move to beginning of file
# f.close()         -> Close file (not needed with 'with')

# ========================================
# IMPORTANT NOTES
# ========================================

# 1. Always use 'with' statement - auto-closes files
# 2. 'r' mode requires file to exist
# 3. readline() includes newline character '\n'
# 4. Use strip() to remove newline: line.strip()
# 5. For large files, use for line in f (not read())
# 6. Handle exceptions (FileNotFoundError, PermissionError)