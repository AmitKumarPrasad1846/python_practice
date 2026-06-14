# Slicing

# Accessing parts of a string

# Syntax:
# str[ starting_idx : ending_idx ]
# # Note: ending_idx is NOT included
str = "ApnaCollege"


# Example 1:
# str[1 : 4] is "pna"
# (Index 1 = 'p', Index 2 = 'n', Index 3 = 'a', stops at Index 4)

# Example 2 (omitting start index):
# str[ : 4 ] is same as str[ 0 : 4 ]  -> "Apna"

# Example 3 (omitting end index):
# str[ 1 : ] is same as str[ 1 : len(str) ]  -> "pnaCollege"

# --- Additional Revision Notes ---

# 1. Negative Indexing in Slicing:
#    str[-4:-1] -> "leg"  (last 3 chars excluding last)
#    str[-4:]   -> "lege" (last 4 chars)

# 2. Slicing with step (skip characters):
#    Syntax: str[start : end : step]

#    Example: str[::2]   -> "AaClee" (every 2nd character)
#    Example: str[1:8:2] -> "pacl"

# 3. Reverse a string using slicing:
#    str[::-1]  -> "egelloCnapA"

# 4. Slicing never gives IndexError:
#    If start/end is out of range, Python adjusts it.
#    Example: str[1:100] -> "pnaCollege" (safe, no error)

# 5. Common use:
#    first_char = str[0]       # indexing
#    first_three = str[:3]     # slicing
#    last_three = str[-3:]     # slicing from end

# Negative Index
str2 = "Apple"
print(str[-3:-1])
print(str[-4:-2])