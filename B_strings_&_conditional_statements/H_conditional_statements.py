# Conditional Statements

# if-elif-else (SYNTAX)

"""
if(condition):
    Statement1
elif(condition):
    Statement2
else:
    StatementN
"""

# --- Additional Revision Notes ---

# 1. Indentation is MANDATORY in Python (usually 4 spaces or a tab)
#    All statements inside a block must be indented equally.

# 2. Example with proper indentation:

age = 18

if age < 18:
    print("Minor")
elif age == 18:
    print("Just became an adult")
else:
    print("Adult")

# 3. if-elif-else flow:
#    - Python checks conditions from top to bottom
#    - Executes the block for the FIRST condition that is True
#    - If no condition is True, executes else block (if present)
#    - Once a block executes, the rest are skipped

# 4. elif is short for "else if" - you can have multiple elif statements

marks = 85

if marks >= 90:
    grade = "A+"
elif marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B"
elif marks >= 60:
    grade = "C"
else:
    grade = "F"

print(f"Grade: {grade}")

# 5. Important syntax rules:
#    - Conditions can be written with or without parentheses:
#        if x > 5:   (works, preferred)
#        if(x > 5):  (also works)
#    - Always end the condition line with a colon (:)
#    - Use indentation to define blocks (no curly braces {} like C/Java)

# 6. Nested conditionals (if inside if):

num = 10

if num > 0:
    print("Positive number")
    if num % 2 == 0:
        print("Also even")
    else:
        print("Also odd")
else:
    print("Negative or zero")

# 7. Ternary operator (shortcut for if-else):
#    value_if_true if condition else value_if_false

age = 20
status = "Adult" if age >= 18 else "Minor"
print(status)  # Output: Adult