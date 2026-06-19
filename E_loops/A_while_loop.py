# Loops in Python

# Loops are used to repeat instructions.

# while Loops

# Syntax:
# while condition:
    # some work (body of loop)
    # update condition to avoid infinite loop

# --- Additional Revision Notes ---

# 1. Basic while loop example:
count = 1
while count <= 5:
    print(count)
    count += 1      # Important: Update condition
# Output: 1, 2, 3, 4, 5

# 2. Infinite loop (BE CAREFUL!):
# while True:
#     print("This will run forever")
# Use Ctrl+C to stop infinite loop

# 3. while loop with break statement:
count = 1
while count <= 10:
    if count == 5:
        break      # Exit loop when count is 5
    print(count)
    count += 1
# Output: 1, 2, 3, 4

# 4. while loop with continue statement:
count = 0
while count < 5:
    count += 1
    if count == 3:
        continue   # Skip rest of loop when count is 3
    print(count)
# Output: 1, 2, 4, 5

# 5. while loop with else:
count = 1
while count <= 3:
    print(count)
    count += 1
else:
    print("Loop completed normally")
# Output: 1, 2, 3, "Loop completed normally"

# 6. Practical examples:

# a) Print numbers from 1 to 10:
i = 1
while i <= 10:
    print(i)
    i += 1

# b) Sum of first n natural numbers:
n = 5
sum = 0
i = 1
while i <= n:
    sum += i
    i += 1
print(f"Sum of 1 to {n} is {sum}")  # Output: 15

# c) Factorial of a number:
num = 5
fact = 1
i = 1
while i <= num:
    fact *= i
    i += 1
print(f"Factorial of {num} is {fact}")  # Output: 120

# d) Print multiplication table:
num = 5
i = 1
while i <= 10:
    print(f"{num} x {i} = {num * i}")
    i += 1

# e) Reverse a number:
num = 12345
rev = 0
while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num //= 10
print(f"Reversed number: {rev}")  # Output: 54321

# f) Check if number is palindrome:
num = 121
temp = num
rev = 0
while temp > 0:
    digit = temp % 10
    rev = rev * 10 + digit
    temp //= 10
if num == rev:
    print("Palindrome")
else:
    print("Not palindrome")

# 7. while with user input (sentinel loop):
total = 0
while True:
    num = int(input("Enter a number (0 to stop): "))
    if num == 0:
        break
    total += num
print(f"Total: {total}")

# 8. Nested while loops:
i = 1
while i <= 3:
    j = 1
    while j <= 3:
        print(f"i={i}, j={j}")
        j += 1
    i += 1

# 9. Common mistakes to avoid:
# - Forgetting to update the loop variable (infinite loop)
# - Off-by-one errors (wrong condition)
# - Using assignment (=) instead of comparison (==)
# - Not handling break/continue properly

# 10. When to use while vs for:
# while: When number of iterations is UNKNOWN (user input, reading files, etc.)
# for: When number of iterations is KNOWN (iterating through sequences)

# for loop preview (will be covered next):
# for i in range(5):
#     print(i)