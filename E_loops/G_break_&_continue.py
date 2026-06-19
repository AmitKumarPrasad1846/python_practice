# Break & Continue

# Break: Used to terminate the loop entirely when encountered.
# Continue: Terminates execution in the current iteration & continues 
#           execution of the loop with the next iteration.

# --- Additional Revision Notes ---

# 1. BREAK - Exits the loop completely:

# Example 1: Break in while loop
i = 1
while i <= 5:
    if i == 3:
        break        # Loop stops when i becomes 3
    print(i)
    i += 1
# Output: 1, 2

# Example 2: Break in for loop
for i in range(1, 6):
    if i == 4:
        break        # Loop stops when i is 4
    print(i)
# Output: 1, 2, 3

# 2. CONTINUE - Skips current iteration, moves to next:

# Example 1: Continue in while loop
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue     # Skips printing 3
    print(i)
# Output: 1, 2, 4, 5

# Example 2: Continue in for loop
for i in range(1, 6):
    if i == 3:
        continue     # Skips printing 3
    print(i)
# Output: 1, 2, 4, 5

# 3. Break vs Continue - Visual Difference:

# BREAK: 
# for i in range(1, 6):
#     if i == 3:
#         break      # STOPS entire loop
#     print(i)
# Output: 1, 2  (loop ends)

# CONTINUE:
# for i in range(1, 6):
#     if i == 3:
#         continue   # SKIPS only iteration 3
#     print(i)
# Output: 1, 2, 4, 5  (loop continues)

# 4. Practical Examples:

# a) Using break to find first even number:
numbers = [1, 3, 5, 7, 8, 9, 10]
for num in numbers:
    if num % 2 == 0:
        print(f"First even number: {num}")
        break
# Output: First even number: 8

# b) Using continue to print only odd numbers:
for i in range(1, 11):
    if i % 2 == 0:
        continue     # Skip even numbers
    print(i)
# Output: 1, 3, 5, 7, 9

# c) Using break in while loop with user input:
while True:
    num = int(input("Enter a number (0 to stop): "))
    if num == 0:
        break        # Exit loop when user enters 0
    print(f"You entered: {num}")

# d) Using continue to skip negative numbers:
numbers = [10, -5, 20, -3, 30, -1, 40]
for num in numbers:
    if num < 0:
        continue     # Skip negative numbers
    print(num)
# Output: 10, 20, 30, 40

# 5. Break in nested loops:
# Break only exits the INNER loop, not the outer loop
for i in range(3):
    for j in range(3):
        if j == 1:
            break    # Breaks inner loop only
        print(f"i={i}, j={j}")
# Output: (0,0), (1,0), (2,0)

# 6. Continue in nested loops:
# Continue affects only the current (innermost) loop
for i in range(3):
    for j in range(3):
        if j == 1:
            continue  # Skips j=1 in inner loop
        print(f"i={i}, j={j}")
# Output: (0,0), (0,2), (1,0), (1,2), (2,0), (2,2)

# 7. Break and Continue with else:
# In loops with else, break prevents else from executing
for i in range(1, 6):
    if i == 3:
        break
    print(i)
else:
    print("Loop completed without break")  # This won't execute

# Without break:
for i in range(1, 6):
    if i == 7:      # Condition never true
        break
    print(i)
else:
    print("Loop completed without break")  # This WILL execute

# 8. Common use cases:
# Break: Search operations, user input termination, finding specific item
# Continue: Filtering unwanted values, skipping invalid data

# 9. Quick reference:
# break -> "Stop the loop entirely"
# continue -> "Skip this iteration and go to next"

# 10. Important notes:
# - break and continue work in BOTH while and for loops
# - In nested loops, break/continue affect only the immediate loop
# - Avoid using continue in while loops without proper condition update
#   (can cause infinite loops)