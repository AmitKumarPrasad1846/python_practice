# ======================================================================
#                    📁 COMPLETE PYTHON FILE I/O + OS MODULE 
#                     Basic → Advanced (Everything You Need)
# ======================================================================

# ======================================================================
# PART 1: BASIC FILE OPERATIONS (Sabse Simple)
# ======================================================================

print("="*60)
print("PART 1: BASIC FILE OPERATIONS")
print("="*60)

# 1.1 WRITE TO FILE ('w' mode - overwrites)
with open("file1.txt", "w") as f:
    f.write("Hello World!\n")
    f.write("This is line 2")

# 1.2 READ ENTIRE FILE ('r' mode)
with open("file1.txt", "r") as f:
    content = f.read()
    print("Content:", content)

# 1.3 APPEND TO FILE ('a' mode - adds to end)
with open("file1.txt", "a") as f:
    f.write("\nThis is appended line")

# 1.4 READ LINE BY LINE
with open("file1.txt", "r") as f:
    for line in f:
        print("Line:", line.strip())

# 1.5 READ ALL LINES INTO LIST
with open("file1.txt", "r") as f:
    lines = f.readlines()
    print("Lines list:", lines)

# ======================================================================
# PART 2: FILE MODES - COMPLETE REFERENCE
# ======================================================================

print("\n" + "="*60)
print("PART 2: FILE MODES")
print("="*60)

"""
'r'  - Read (file must exist)
'w'  - Write (overwrites, creates if not exists)
'a'  - Append (adds to end, creates if not exists)
'x'  - Exclusive create (fails if exists)
'r+' - Read + Write (file must exist)
'w+' - Write + Read (overwrites, creates if not exists)
'a+' - Append + Read (creates if not exists)
'rb' - Read Binary
'wb' - Write Binary
'ab' - Append Binary
"""

# Example: 'x' mode
try:
    with open("newfile.txt", "x") as f:
        f.write("Brand new file")
except FileExistsError:
    print("File already exists!")

# ======================================================================
# PART 3: HANDLING ERRORS (Professional Way)
# ======================================================================

print("\n" + "="*60)
print("PART 3: ERROR HANDLING")
print("="*60)

def safe_read_file(filename):
    """Professional error handling for file reading"""
    try:
        with open(filename, 'r') as f:
            return f.read()
    except FileNotFoundError:
        print(f"❌ Error: '{filename}' not found!")
        return None
    except PermissionError:
        print(f"❌ Error: Permission denied for '{filename}'!")
        return None
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return None

# Test it
content = safe_read_file("nonexistent.txt")

# ======================================================================
# PART 4: WORKING WITH DIFFERENT FILE TYPES
# ======================================================================

print("\n" + "="*60)
print("PART 4: DIFFERENT FILE TYPES")
print("="*60)

# 4.1 CSV FILES (Excel style)
import csv

# Write CSV
data = [
    ['Name', 'Age', 'City'],
    ['Amit', 25, 'Delhi'],
    ['Priya', 22, 'Mumbai'],
    ['Raj', 30, 'Bangalore']
]

with open('users.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(data)

# Read CSV
with open('users.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# Read CSV as dictionary
with open('users.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(f"{row['Name']} is {row['Age']} years old")

# 4.2 JSON FILES (API/Data storage)
import json

# Write JSON
data = {
    "name": "Amit",
    "age": 25,
    "city": "Delhi",
    "hobbies": ["reading", "gaming", "coding"]
}

with open('data.json', 'w') as f:
    json.dump(data, f, indent=4)

# Read JSON
with open('data.json', 'r') as f:
    loaded = json.load(f)
    print(f"Name: {loaded['name']}")
    print(f"Hobbies: {loaded['hobbies']}")

# 4.3 BINARY FILES (Images, Audio, Video)
# Write binary data
binary_data = b'\x00\x01\x02\x03\x04'
with open('binary.bin', 'wb') as f:
    f.write(binary_data)

# Read binary data
with open('binary.bin', 'rb') as f:
    data = f.read()
    print(f"Binary data: {data}")

# ======================================================================
# PART 5: OS MODULE - FILES & FOLDERS
# ======================================================================

print("\n" + "="*60)
print("PART 5: OS MODULE - FILES & FOLDERS")
print("="*60)

import os

# 5.1 BASIC OPERATIONS
print("\n--- Basic Operations ---")

# Create folder
os.makedirs("my_project", exist_ok=True)
print("✅ Folder created: my_project")

# Get current directory
current_dir = os.getcwd()
print(f"📍 Current directory: {current_dir}")

# List files
files = os.listdir(".")
print(f"📂 Files in current dir: {files}")

# Check if file/folder exists
if os.path.exists("my_project"):
    print("✅ my_project exists!")

# Check if it's a file or folder
if os.path.isdir("my_project"):
    print("✅ my_project is a folder")
if os.path.isfile("file1.txt"):
    print("✅ file1.txt is a file")

# 5.2 PATH OPERATIONS
print("\n--- Path Operations ---")

# Join paths (cross-platform safe)
path = os.path.join("my_project", "data", "file.txt")
print(f"Path: {path}")

# Get file info
file_path = "file1.txt"
print(f"File name: {os.path.basename(file_path)}")
print(f"Folder name: {os.path.dirname(file_path)}")
filename, ext = os.path.splitext(file_path)
print(f"Filename: {filename}, Extension: {ext}")

# Absolute path
abs_path = os.path.abspath(file_path)
print(f"Absolute path: {abs_path}")

# 5.3 FILE INFORMATION
print("\n--- File Information ---")

if os.path.exists("file1.txt"):
    size = os.path.getsize("file1.txt")
    print(f"Size: {size} bytes")
    
    import time
    modified = os.path.getmtime("file1.txt")
    print(f"Modified: {time.ctime(modified)}")

# 5.4 RENAME AND DELETE
print("\n--- Rename & Delete ---")

# Create temp file
with open("temp.txt", "w") as f:
    f.write("Temporary file")

# Rename
os.rename("temp.txt", "temp_renamed.txt")
print("✅ File renamed")

# Delete
if os.path.exists("temp_renamed.txt"):
    os.remove("temp_renamed.txt")
    print("✅ File deleted")

# 5.5 SYSTEM INFORMATION
print("\n--- System Information ---")

print(f"OS Name: {os.name}")
print(f"CPU Cores: {os.cpu_count()}")
print(f"Path Separator: {os.sep}")
print(f"Newline: {repr(os.linesep)}")

# 5.6 ENVIRONMENT VARIABLES
print("\n--- Environment Variables ---")

print(f"PATH: {os.environ.get('PATH', 'Not set')[:50]}...")
os.environ['MY_VAR'] = 'Hello'
print(f"MY_VAR: {os.environ['MY_VAR']}")

# ======================================================================
# PART 6: ADVANCED FILE OPERATIONS (shutil)
# ======================================================================

print("\n" + "="*60)
print("PART 6: ADVANCED FILE OPERATIONS (shutil)")
print("="*60)

import shutil

# Create test files
with open("source.txt", "w") as f:
    f.write("This is source file")
with open("dest.txt", "w") as f:
    f.write("This is destination file")

# 6.1 COPY FILES
shutil.copy("source.txt", "source_copy.txt")
print("✅ File copied")

# 6.2 COPY FOLDER
os.makedirs("source_folder", exist_ok=True)
with open("source_folder/test.txt", "w") as f:
    f.write("Test file in folder")
shutil.copytree("source_folder", "dest_folder")
print("✅ Folder copied")

# 6.3 MOVE FILES/FOLDERS
shutil.move("source_copy.txt", "moved_file.txt")
print("✅ File moved")

# 6.4 DELETE FOLDER (with all contents)
shutil.rmtree("dest_folder")
print("✅ Folder deleted")

# 6.5 DISK SPACE
total, used, free = shutil.disk_usage("/")
print(f"Total: {total//(2**30)} GB")
print(f"Free: {free//(2**30)} GB")

# ======================================================================
# PART 7: WALK() - RECURSIVE FOLDER TRAVERSAL
# ======================================================================

print("\n" + "="*60)
print("PART 7: WALK() - RECURSIVE FOLDER TRAVERSAL")
print("="*60)

# Create some folders and files
os.makedirs("project/src", exist_ok=True)
os.makedirs("project/data", exist_ok=True)
with open("project/src/main.py", "w") as f:
    f.write("print('Hello')")
with open("project/data/input.txt", "w") as f:
    f.write("Data here")

# Walk through all files
def list_all_files(folder):
    """Show all files in folder recursively"""
    print(f"\n📂 Exploring: {folder}")
    for root, dirs, files in os.walk(folder):
        level = root.replace(folder, '').count(os.sep)
        indent = '  ' * level
        print(f"{indent}📁 {os.path.basename(root)}/")
        for file in files:
            print(f"{indent}  📄 {file}")

list_all_files("project")

# ======================================================================
# PART 8: TEMPORARY FILES (For testing)
# ======================================================================

print("\n" + "="*60)
print("PART 8: TEMPORARY FILES")
print("="*60)

import tempfile

# 8.1 Temporary File
with tempfile.NamedTemporaryFile(mode='w', delete=True) as temp:
    temp.write("Temporary data")
    temp.seek(0)
    print("Temp file content:", temp.read())
    print("Temp file name:", temp.name)
# File automatically deleted

# 8.2 Temporary Directory
with tempfile.TemporaryDirectory() as temp_dir:
    print("Temp directory:", temp_dir)
    with open(os.path.join(temp_dir, "test.txt"), "w") as f:
        f.write("Hello")
# Directory automatically deleted

# ======================================================================
# PART 9: FILE SEARCH & FILTER
# ======================================================================

print("\n" + "="*60)
print("PART 9: FILE SEARCH & FILTER")
print("="*60)

def find_files_by_extension(ext, folder="."):
    """Find all files with given extension"""
    matches = []
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith(ext):
                matches.append(os.path.join(root, file))
    return matches

print("Text files:", find_files_by_extension(".txt"))
print("Python files:", find_files_by_extension(".py"))

def find_large_files(folder, size_limit_mb=1):
    """Find files larger than size limit"""
    large_files = []
    for root, dirs, files in os.walk(folder):
        for file in files:
            file_path = os.path.join(root, file)
            size = os.path.getsize(file_path)
            if size > size_limit_mb * 1024 * 1024:
                large_files.append((file_path, size))
    return large_files

print("Large files:", find_large_files(".", 0.001))

# ======================================================================
# PART 10: REAL-WORLD PROJECT - FILE ORGANIZER
# ======================================================================

print("\n" + "="*60)
print("PART 10: FILE ORGANIZER - REAL PROJECT")
print("="*60)

def organize_files_by_extension(folder_path):
    """
    Organize files by extension into separate folders.
    Like: downloads -> images/, documents/, videos/, etc.
    """
    if not os.path.exists(folder_path):
        print(f"❌ Folder not found: {folder_path}")
        return
    
    # Define categories
    categories = {
        'images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
        'documents': ['.pdf', '.doc', '.docx', '.txt', '.xlsx', '.csv'],
        'videos': ['.mp4', '.mov', '.avi', '.mkv'],
        'audio': ['.mp3', '.wav', '.aac'],
        'archives': ['.zip', '.rar', '.tar', '.gz'],
        'code': ['.py', '.java', '.cpp', '.html', '.css', '.js'],
    }
    
    # Files ko move karo
    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)
        
        # Skip folders
        if os.path.isdir(file_path):
            continue
        
        # Extension find karo
        _, ext = os.path.splitext(file)
        ext = ext.lower()
        
        # Category find karo
        target_folder = 'others'
        for category, extensions in categories.items():
            if ext in extensions:
                target_folder = category
                break
        
        # Folder banayo
        dest_folder = os.path.join(folder_path, target_folder)
        os.makedirs(dest_folder, exist_ok=True)
        
        # File move karo
        dest_path = os.path.join(dest_folder, file)
        shutil.move(file_path, dest_path)
        print(f"✅ Moved: {file} -> {target_folder}/")

# Test create some files
os.makedirs("downloads", exist_ok=True)
with open("downloads/photo.jpg", "w") as f: f.write("test")
with open("downloads/doc.pdf", "w") as f: f.write("test")
with open("downloads/video.mp4", "w") as f: f.write("test")
with open("downloads/script.py", "w") as f: f.write("test")

# Run organizer
organize_files_by_extension("downloads")

# ======================================================================
# PART 11: BONUS - FILE BACKUP SYSTEM
# ======================================================================

print("\n" + "="*60)
print("PART 11: FILE BACKUP SYSTEM")
print("="*60)

from datetime import datetime

def backup_file(file_path):
    """Create backup with timestamp"""
    if not os.path.exists(file_path):
        print(f"❌ File not found: {file_path}")
        return False
    
    # Backup name banayein
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = f"{file_path}.backup_{timestamp}"
    
    # Copy karo
    shutil.copy(file_path, backup_path)
    print(f"✅ Backup created: {backup_path}")
    return True

# Test
with open("important.txt", "w") as f:
    f.write("Important data")
backup_file("important.txt")

# ======================================================================
# PART 12: BONUS - LOGGING SYSTEM
# ======================================================================

print("\n" + "="*60)
print("PART 12: LOGGING SYSTEM")
print("="*60)

import logging

# Setup logging
logging.basicConfig(
    filename='app.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Use it
logging.info("Application started")
logging.warning("This is a warning")
logging.error("This is an error")
print("✅ Logs saved to app.log")

# ======================================================================
# PART 13: COMPLETE CHEAT SHEET
# ======================================================================

print("\n" + "="*60)
print("PART 13: QUICK REFERENCE CHEAT SHEET")
print("="*60)

cheat_sheet = """
📁 FILE OPERATIONS
-----------------
open('file', 'r')      -> Read file
open('file', 'w')      -> Write (overwrite)
open('file', 'a')      -> Append
open('file', 'x')      -> Create new
open('file', 'rb')     -> Read binary
open('file', 'wb')     -> Write binary

📄 READING FILES
---------------
f.read()               -> Entire file
f.readline()           -> One line
f.readlines()          -> All lines as list
for line in f:         -> Loop through lines

📝 WRITING FILES
---------------
f.write('text')        -> Write string
f.writelines(list)     -> Write list
f.write('\\n')          -> New line

📂 OS MODULE
------------
os.mkdir('folder')     -> Create folder
os.rmdir('folder')     -> Delete empty folder
os.rename('old','new') -> Rename
os.remove('file')      -> Delete file
os.listdir('.')        -> List files
os.path.exists('f')    -> Check exists
os.path.join('a','b')  -> Join paths
os.getcwd()            -> Current path
os.chdir('path')       -> Change path

📊 OS INFO
----------
os.name                -> OS name
os.cpu_count()         -> CPU cores
os.environ             -> Env variables
os.system('cmd')       -> Run system command

📦 SHUTIL (ADVANCED)
-------------------
shutil.copy(src,dst)   -> Copy file
shutil.move(src,dst)   -> Move file
shutil.copytree(src,dst) -> Copy folder
shutil.rmtree(path)    -> Delete folder
shutil.disk_usage('/') -> Disk space

🔍 WALK
--------
os.walk('folder')      -> Traverse all files/folders
"""

print(cheat_sheet)

# ======================================================================
# PART 14: CLEANUP - Delete all test files
# ======================================================================

print("\n" + "="*60)
print("PART 14: CLEANUP")
print("="*60)

# Delete all test files and folders
def cleanup():
    """Delete all test files/folders created by this tutorial"""
    test_items = [
        "file1.txt", "users.csv", "data.json", "binary.bin",
        "source.txt", "dest.txt", "moved_file.txt", "important.txt",
        "newfile.txt", "source_folder", "project", "downloads",
        "my_project", "app.log"
    ]
    for item in test_items:
        try:
            if os.path.exists(item):
                if os.path.isdir(item):
                    shutil.rmtree(item)
                    print(f"🗑️ Deleted folder: {item}")
                else:
                    os.remove(item)
                    print(f"🗑️ Deleted file: {item}")
        except Exception as e:
            print(f"⚠️ Could not delete {item}: {e}")

cleanup()

print("\n" + "="*60)
print("✅ COMPLETE TUTORIAL FINISHED!")
print("🎉 You now know File I/O + OS Module from Basic to Advanced!")
print("="*60)