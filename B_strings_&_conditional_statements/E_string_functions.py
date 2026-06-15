# String Functions

str = "I am a coder."

# 1. endswith() - Returns True if string ends with the specified substring
str.endswith("er.")   # Returns: True
str.endswith("xyz")   # Returns: False

# 2. capitalize() - Capitalizes the first character of the string
str.capitalize()      # Returns: "i am a coder." (Note: first char becomes uppercase)
                      # Original string remains unchanged (strings are immutable)

# 3. replace() - Replaces all occurrences of old substring with new substring
str.replace("a", "X") # Returns: "I Xm X coder."
str.replace("am", "was") # Returns: "I was a coder."

# 4. find() - Returns the first index of the first occurrence of the substring
str.find("am")        # Returns: 2 (index where "am" starts)
str.find("coder")     # Returns: 7
str.find("xyz")       # Returns: -1 (not found)

# 5. count() - Counts the number of occurrences of a substring in the string
str.count("a")        # Returns: 2 (one 'a' in "am", one 'a' in "coder")
str.count("am")       # Returns: 1

# --- Additional Revision Notes ---

# 6. upper() and lower() - Change case of entire string
str.upper()           # Returns: "I AM A CODER."
str.lower()           # Returns: "i am a coder."

# 7. strip() - Removes leading/trailing whitespace
"  hello  ".strip()   # Returns: "hello"

# 8. split() - Splits string into a list
str.split()           # Returns: ['I', 'am', 'a', 'coder.']
str.split("a")        # Returns: ['I ', 'm ', ' coder.']

# 9. join() - Joins elements of a list into a string
"-".join(["apple", "banana", "cherry"])  # Returns: "apple-banana-cherry"

# 10. len() - Returns length of string (built-in function)
len(str)              # Returns: 13

# 11. in operator - Check if substring exists
"coder" in str        # Returns: True
"python" in str       # Returns: False

# Important: Most string functions return a NEW string and do not modify the original
# because strings are immutable in Python.