# ========================================
# WITH STATEMENT - QUICK REVISION
# ========================================

# Syntax:
with open("demo.txt", "a") as f:
    data = f.read()

# ========================================
# WHAT IT DOES?
# ========================================

# 1. Automatically opens the file
# 2. Performs the operation (read/write/append)
# 3. Automatically CLOSES the file (no need to write f.close())

# ========================================
# WITHOUT 'with' (Old way)
# ========================================

f = open("demo.txt", "a")
data = f.read()
f.close()  # ❌ Have to close manually

# ========================================
# WITH 'with' (Best way)
# ========================================

with open("demo.txt", "a") as f:
    data = f.read()
# ✅ File automatically closed!

# ========================================
# WHY USE 'with'?
# ========================================

# 1. ✅ No need to write f.close()
# 2. ✅ File closes even if error occurs
# 3. ✅ Cleaner code
# 4. ✅ Industry standard

# ========================================
# DIFFERENT MODES WITH 'with'
# ========================================

# Read
with open("file.txt", "r") as f:
    data = f.read()

# Write
with open("file.txt", "w") as f:
    f.write("Hello")

# Append
with open("file.txt", "a") as f:
    f.write("World")

# Binary
with open("file.jpg", "rb") as f:
    data = f.read()

# ========================================
# MULTIPLE FILES
# ========================================

with open("input.txt", "r") as f1, open("output.txt", "w") as f2:
    data = f1.read()
    f2.write(data)

# ========================================
# REMEMBER
# ========================================

# 'with' = Open + Auto-close
# Best practice for file handling