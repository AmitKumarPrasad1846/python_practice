# ========================================
# PRACTICE - TRY THESE
# ========================================

import os

# 1. Create a file
with open("test_delete.txt", "w") as f:
    f.write("Hello")

# 2. Check if it exists
print(os.path.exists("test_delete.txt"))  # True

# 3. Delete it
os.remove("test_delete.txt")

# 4. Check again
print(os.path.exists("test_delete.txt"))  # False

print("✅ Practice complete!")