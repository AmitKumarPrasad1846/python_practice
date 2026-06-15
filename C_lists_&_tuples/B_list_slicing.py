# List Slicing

# Similar to String Slicing

# Syntax:
# list_name[starting_idx : ending_idx]   # ending_idx is NOT included

marks = [87, 64, 33, 95, 76]

# Examples:
marks[1 : 4]    # Returns: [64, 33, 95]  (indices 1, 2, 3)
marks[: 4]      # Same as marks[0 : 4]   -> [87, 64, 33, 95]
marks[1 :]      # Same as marks[1 : len(marks)] -> [64, 33, 95, 76]
marks[-3 : -1]  # Returns: [33, 95]      (indices -3, -2)

# --- Additional Revision Notes ---

# 1. List slicing creates a NEW list (doesn't modify original)
original = [10, 20, 30, 40, 50]
sliced = original[1:4]   # [20, 30, 40]
print(original)           # [10, 20, 30, 40, 50] (unchanged)

# 2. Slicing with step (skip elements):
# Syntax: list[start : end : step]
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers[::2]      # [1, 3, 5, 7, 9]   (every 2nd element)
numbers[1::2]     # [2, 4, 6, 8, 10]  (every 2nd element starting from index 1)
numbers[2:8:2]    # [3, 5, 7]         (from index 2 to 7, step 2)

# 3. Negative step (reverse traversal):
numbers[::-1]     # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1] (reverse the list)
numbers[5:1:-1]   # [6, 5, 4, 3]       (from index 5 down to 2)
numbers[-2:-5:-1] # [9, 8, 7]         (from -2 to -5, reverse)

# 4. Slicing never gives IndexError:
# If indices are out of range, Python adjusts them automatically
marks[1:100]      # [64, 33, 95, 76]  (safe, no error)
marks[-10:3]      # [87, 64, 33]      (starts from beginning)

# 5. Modifying lists using slicing:
# Replace a slice with new values
marks[1:3] = [100, 200]   # [87, 100, 200, 95, 76]
# Delete a slice
marks[1:3] = []           # [87, 95, 76]

# 6. Copying a list using slicing:
new_list = marks[:]       # Creates a full copy (different from just assigning)
# Without [:] - both variables point to the same list
copy1 = marks             # Both refer to same list (shallow reference)
copy2 = marks[:]          # New independent list

# 7. Practical examples:
colors = ["red", "blue", "green", "yellow", "purple"]
first_two = colors[:2]        # ["red", "blue"]
last_two = colors[-2:]        # ["yellow", "purple"]
middle_three = colors[1:4]    # ["blue", "green", "yellow"]
every_other = colors[::2]     # ["red", "green", "purple"]

# 8. Difference from String Slicing:
# - String slicing returns a STRING (immutable)
# - List slicing returns a LIST (mutable)
# - Both follow same index/slice rules