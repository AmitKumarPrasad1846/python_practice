# Write a function that returns factorial of n

# def factorial(n):
#     # Your code here
#     result = 1
#     for i in range(1, n+1):
#         result*=i
#     return result
    # pass

# Test cases:
# print(factorial(0))  # Should print 1
# print(factorial(1))  # Should print 1
# print(factorial(5))  # Should print 120

# ======================================================
# Calculate: 1! + 2! + 3! + ... + n!
# def sum_of_factorials(n):
#     total = 0
#     for i in range(1, n+1):
#         total += factorial(i)  # Reuse the factorial function
#     return total

# print(sum_of_factorials(3))  # 1!+2!+3! = 1+2+6 = 9

# ======================================================
# Create a list of factorials from 0 to n
# def factorial_list(n):
#     result = []
#     for i in range(n+1):
#         result.append(factorial(i))
#     return result

# print(factorial_list(5))  # [1, 1, 2, 6, 24, 120]

# ======================================================
# ======================================================

# 1. Calculate n! using ONLY while loop (no for)
n = int(input("Enter a number : "))
i, result = (1, 1)

while i<=n:
    result *= i
    i+=1
print(result)

# ========================================================

# 2. Calculate n! without using * operator (use addition)
# function to multiply two numbers using addition...
def multiply(a, b):
    result = 0
    for a in range(b):
        result += a
    return result

# factorial using addition only
def factorial(n):
    result = 1
    for i in range(1, n+1):
        result = multiply(result, i)
    return result

# testing cases
print(factorial(0))
print(factorial(1))
print(factorial(5))

# =========================================================

# 3. Find the first n numbers where factorial is > 1000

def factorial(a):
    result = 0
    for i in range(1, n+1):
        result *= i
    return result



# =========================================================

# 4. Create a function that returns the factorial of each digit in a number
