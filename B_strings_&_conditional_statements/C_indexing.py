# Indexing

# In Python, strings are indexed starting from 0.
# Example string:
string = "Apna_College"

# Index positions:
# 0:'A', 1:'p', 2:'n', 3:'a', 4:'_', 5:'C', 6:'o', 7:'l', 8:'l', 9:'e', 10:'g', 11:'e'

# Accessing characters using index:
# str[0] is 'A'
# str[1] is 'p'
# ... and so on.

# Important Note: Strings are immutable in Python.
# This means you cannot change a specific character using assignment.
# Example (This will cause an error):
# str[0] = 'B'   # NOT allowed -> TypeError: 'str' object does not support item assignment

# --- Additional Revision Notes ---
# 1. Positive Indexing: Starts from 0 (left to right).
# 2. Negative Indexing: Starts from -1 (right to left).
#    Example: str[-1] is 'e', str[-2] is 'e', str[-3] is 'g'
# 3. To modify a string, you must create a new one:
#    new_str = 'B' + str[1:]   # This works: 'Bpna_College'
# 4. len(str) returns the length of the string (here: 12)
# 5. IndexError occurs if you try to access an index out of range (e.g., str[12])

str = "Amit Kumar Prasad"
print(str[2])
print(str[7])
print(str[5])

# using string indexing we can only read the index values. we can't change or manipulate that.

