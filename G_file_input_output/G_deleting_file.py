# ========================================
# DELETING A FILE IN PYTHON
# ========================================

# Using the OS Module
# Module = A code library written by other programmers
# Contains functions we can use

import os

# Basic syntax
os.remove("filename.txt")

# ========================================
# WHAT IS A MODULE?
# ========================================

"""
Module = A file containing Python code (functions, classes, variables)
Written by other programmers to make our life easier

Examples:
- os module → Operating system functions
- math module → Mathematical functions
- random module → Random number generation
- datetime module → Date and time functions
"""

# ========================================
# STEP 1: IMPORT THE OS MODULE
# ========================================

import os  # Import karo pehle

# Now you can use all os functions

# ========================================
# STEP 2: DELETE A FILE
# ========================================

# Simple delete
os.remove("file.txt")

# With path
os.remove("folder/file.txt")

# ========================================
# SAFE DELETE - CHECK IF FILE EXISTS
# ========================================

# Method 1: Check before deleting
if os.path.exists("file.txt"):
    os.remove("file.txt")
    print("✅ File deleted successfully!")
else:
    print("❌ File not found!")

# Method 2: Using try-except (Professional way)
try:
    os.remove("file.txt")
    print("✅ File deleted successfully!")
except FileNotFoundError:
    print("❌ File not found!")
except PermissionError:
    print("❌ Permission denied!")
except Exception as e:
    print(f"❌ Error: {e}")

# ========================================
# MULTIPLE FILES DELETE
# ========================================

# Delete multiple files
files_to_delete = ["file1.txt", "file2.txt", "file3.txt"]

for file in files_to_delete:
    if os.path.exists(file):
        os.remove(file)
        print(f"✅ Deleted: {file}")
    else:
        print(f"❌ Not found: {file}")

# ========================================
# DELETE ALL FILES WITH SPECIFIC EXTENSION
# ========================================

# Delete all .txt files
import os

for file in os.listdir("."):
    if file.endswith(".txt"):
        os.remove(file)
        print(f"✅ Deleted: {file}")

# Delete all .log files in a folder
folder = "logs"
for file in os.listdir(folder):
    if file.endswith(".log"):
        os.remove(os.path.join(folder, file))
        print(f"✅ Deleted: {file}")

# ========================================
# DELETE FILES OLDER THAN X DAYS
# ========================================

import os
import time
from datetime import datetime, timedelta

def delete_old_files(folder, days=30):
    """Delete files older than 'days'"""
    cutoff_time = time.time() - (days * 24 * 60 * 60)
    
    for file in os.listdir(folder):
        file_path = os.path.join(folder, file)
        if os.path.isfile(file_path):
            file_age = os.path.getmtime(file_path)
            if file_age < cutoff_time:
                os.remove(file_path)
                print(f"✅ Deleted old file: {file}")

# Use it
delete_old_files("logs", 7)  # Delete files older than 7 days

# ========================================
# DELETE EMPTY FILES
# ========================================

def delete_empty_files(folder):
    """Delete all empty files in a folder"""
    for file in os.listdir(folder):
        file_path = os.path.join(folder, file)
        if os.path.isfile(file_path) and os.path.getsize(file_path) == 0:
            os.remove(file_path)
            print(f"✅ Deleted empty file: {file}")

# ========================================
# DELETE FOLDER (WITH ALL CONTENTS)
# ========================================

import shutil

# Delete empty folder
os.rmdir("empty_folder")  # Only if empty

# Delete folder with all contents (⚠️ Dangerous!)
shutil.rmtree("folder_to_delete")  # Permanently deletes everything!

# Safe folder delete
def safe_delete_folder(folder):
    confirm = input(f"Delete '{folder}' and all contents? (y/n): ")
    if confirm.lower() == 'y':
        shutil.rmtree(folder)
        print(f"✅ Deleted: {folder}")
    else:
        print("❌ Cancelled")

# ========================================
# COMPLETE FILE MANAGEMENT CLASS
# ========================================

import os
import shutil
from datetime import datetime

class FileManager:
    """Professional file management system"""
    
    def __init__(self, folder="."):
        self.folder = folder
    
    def delete_file(self, filename):
        """Delete a file safely"""
        file_path = os.path.join(self.folder, filename)
        try:
            if os.path.exists(file_path):
                os.remove(file_path)
                print(f"✅ Deleted: {filename}")
                return True
            else:
                print(f"❌ Not found: {filename}")
                return False
        except Exception as e:
            print(f"❌ Error deleting {filename}: {e}")
            return False
    
    def delete_files_by_extension(self, ext):
        """Delete all files with specific extension"""
        count = 0
        for file in os.listdir(self.folder):
            if file.endswith(ext):
                file_path = os.path.join(self.folder, file)
                try:
                    os.remove(file_path)
                    count += 1
                    print(f"✅ Deleted: {file}")
                except:
                    print(f"❌ Failed: {file}")
        print(f"🗑️ Total deleted: {count} files")
        return count
    
    def delete_empty_files(self):
        """Delete all empty files"""
        count = 0
        for file in os.listdir(self.folder):
            file_path = os.path.join(self.folder, file)
            if os.path.isfile(file_path) and os.path.getsize(file_path) == 0:
                os.remove(file_path)
                count += 1
                print(f"✅ Deleted empty file: {file}")
        print(f"🗑️ Total empty files deleted: {count}")
        return count
    
    def delete_old_files(self, days=30):
        """Delete files older than X days"""
        cutoff = time.time() - (days * 24 * 60 * 60)
        count = 0
        for file in os.listdir(self.folder):
            file_path = os.path.join(self.folder, file)
            if os.path.isfile(file_path):
                if os.path.getmtime(file_path) < cutoff:
                    os.remove(file_path)
                    count += 1
                    print(f"✅ Deleted old file: {file}")
        print(f"🗑️ Total old files deleted: {count}")
        return count

# How to use:
# fm = FileManager("downloads")
# fm.delete_file("temp.txt")
# fm.delete_files_by_extension(".log")
# fm.delete_empty_files()
# fm.delete_old_files(7)

# ========================================
# DELETE VS OTHER OPERATIONS - COMPARISON
# ========================================

"""
Function          | What it does
------------------|----------------------------------------
os.remove()       | Delete a single file
os.rmdir()        | Delete empty folder
shutil.rmtree()   | Delete folder + all contents
os.rename()       | Rename file/folder
shutil.move()     | Move file/folder
shutil.copy()     | Copy file
"""

# ========================================
# COMMON MISTAKES & SOLUTIONS
# ========================================

# ❌ MISTAKE 1: Deleting without checking
os.remove("file.txt")  # Error if file doesn't exist

# ✅ SOLUTION: Check first
if os.path.exists("file.txt"):
    os.remove("file.txt")

# ❌ MISTAKE 2: Using wrong path
os.remove("folder/file.txt")  # Error if folder doesn't exist

# ✅ SOLUTION: Use os.path.join
file_path = os.path.join("folder", "file.txt")
if os.path.exists(file_path):
    os.remove(file_path)

# ❌ MISTAKE 3: Deleting a folder with files
os.rmdir("folder")  # Error if not empty

# ✅ SOLUTION: Use shutil.rmtree() or delete files first
shutil.rmtree("folder")  # Deletes everything

# ========================================
# REAL-WORLD USE CASES
# ========================================

# 1. Clean up temporary files
def cleanup_temp():
    temp_files = ["temp.log", "cache.txt", "backup.tmp"]
    for file in temp_files:
        if os.path.exists(file):
            os.remove(file)
    print("🧹 Temp files cleaned!")

# 2. Delete old backup files
def cleanup_backups(keep=5):
    """Keep only latest 5 backups, delete rest"""
    backups = [f for f in os.listdir(".") if f.startswith("backup_")]
    backups.sort()
    for backup in backups[:-keep]:
        os.remove(backup)
        print(f"✅ Deleted old backup: {backup}")

# 3. Safe delete with confirmation
def confirm_delete(filename):
    response = input(f"Delete '{filename}'? (y/n): ")
    if response.lower() == 'y':
        if os.path.exists(filename):
            os.remove(filename)
            print(f"✅ Deleted: {filename}")
        else:
            print(f"❌ Not found: {filename}")
    else:
        print("❌ Cancelled")

# ========================================
# QUICK REFERENCE
# ========================================

# Import
import os

# Check if file exists
os.path.exists("file.txt")

# Delete file
os.remove("file.txt")

# Safe delete
if os.path.exists("file.txt"):
    os.remove("file.txt")

# Delete with error handling
try:
    os.remove("file.txt")
except FileNotFoundError:
    print("File not found")

# Delete folder with contents
import shutil
shutil.rmtree("folder")

# ========================================
# IMPORTANT NOTES
# ========================================

# 1. Deleting is PERMANENT! No recycle bin!
# 2. Always check if file exists before deleting
# 3. Use try-except for error handling
# 4. Be careful with wildcard deletions (*.txt)
# 5. Test with non-important files first
# 6. shutil.rmtree() is dangerous - use with caution
# 7. On Windows, open files can't be deleted