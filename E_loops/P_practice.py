# WAP to find the sum of first n numbers. (using while)

# n = int(input("How many sums you want? = "))
# sum = {n*(n+1)/2}

# print(f"the sum of {n} numbers is = {sum}")

# =====================================
n = int(input("Enter n: "))
i = 1
sum = 0
while i <= n:
    sum += i
    i += 1
print("Sum of first", n, "numbers is:", sum)
