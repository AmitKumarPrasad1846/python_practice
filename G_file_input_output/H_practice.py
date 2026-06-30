with open("H_practice.txt", "a+") as file:
    file.write("Hi everyone\n")
    file.write("we are learning file I/O\n")
    file.write("using Java.\n")
    file.write("I like programming in java.")

# ========================================================

with open("H_practice.txt", "r") as f:
    data = f.read()

new_data = data.replace("Java", "Python").replace("java", "python")
print(new_data)

# =========================================================

word = "learning"
with open("H_practice.txt", "r") as o:
    reading = o.read()

if (reading.find(word) != -1):
    print("found")
else:
    print("not found")

# my learnings
# 📘 Notes on str.replace() and Case Sensitivity

# Problem:
# - str.replace() in Python is case-sensitive.
# - "Java" (capital J) will be replaced, but "java" (lowercase j) will not.

# Solutions:

# 1. Replace both cases separately
new_data = data.replace("Java", "Python").replace("java", "Python")

# 2. Case-insensitive replacement using regex
import re
new_data = re.sub(r"java", "Python", data, flags=re.IGNORECASE)
# This replaces both "Java" and "java" with "Python".

# 3. Normalize case before replacing
new_data = data.lower().replace("java", "python")
# ⚠️ This makes the entire text lowercase, so capitalization is lost.

# ✅ Key Takeaway:
# - str.replace() only matches exact case.
# - Use multiple replace calls or regex for case-insensitive replacement.
# - Lowercasing works if you don’t care about preserving original capitalization.
