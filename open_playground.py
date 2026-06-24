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
# n = int(input("Enter a number : "))
# i, result = (1, 1)

# while i<=n:
#     result *= i
#     i+=1
# print(result)

# ========================================================

# 2. Calculate n! without using * operator (use addition)
# function to multiply two numbers using addition...
# def multiply(a, b):
#     result = 0
#     for a in range(b):
#         result += a
#     return result

# # factorial using addition only
# def factorial(n):
#     result = 1
#     for i in range(1, n+1):
#         result = multiply(result, i)
#     return result

# # testing cases
# print(factorial(0))
# print(factorial(1))
# print(factorial(5))

# =========================================================

# 3. Find the first n numbers where factorial is > 1000

# def factorial(a):
#     result = 0
#     for i in range(1, n+1):
#         result *= i
#     return result



# =========================================================

# 4. Create a function that returns the factorial of each digit in a number


# =========================================================

# writting inside a file

# file = open("my_file.txt", "w")
# file.write("hello world! I am amit & I am learing to code in python...")

# file.close()

# Reading a file

# file = open("my_file.txt", "r")

# content = file.read()
# print(content)
# file.close()

# Adding contents inside the file

# file = open("my_file.txt", "a")
# file.write("right now I am in my 1st year of college.")
# file.write("Actually the irony in my college is all of my teachers are telling me that do focus on syllabus and don't knwo what to do with that and that syllabus for me is like a crunch of only 2 days.")
# file.write("Whenever I tell my teachers that currently I am learing this and that language or coding IDK what happens to them but there faces seems like they dont even understand a sigle word whatever I ama sayin to the.")
# file.write("As you all know all the fingers are not same hence here in my college there a few teachers who supports me. It would be my pleasure to name such amazing teacher!")
# file.write("Mr. Divyanshu Wagh sir - He is such a great teacher who teaches me each and everything and really his actions me everytime whenever he gives me some unique idea")
# file.write("Ummm...")
# file.write("there are other 1, 2 teacher who supports me in doing decision making but they are not like Divyanshu wagh sir")

# file.write("but..but..but..")
# file.write("I don't even care what they are saying because i have my greatest supporter whos hands all upon me whenever I feel that I am alone i.e. 'my papa'")

# file.close()

# Best method to Open and close files.
# using "with" it automatically opens and closes the files.

# writting
# with open("my_file2.txt", "w") as file:
#     file.write("Hi I am Amit...")

# reading
# with open("my_file2.txt", "r") as file:
#     print(file.read())

# append
# with open("my_file2.txt", "a") as file:
#     print(file.write("\nNew line added!"))

# while using the with statement no need to write file.close() - as with statement automatically closes the file.

