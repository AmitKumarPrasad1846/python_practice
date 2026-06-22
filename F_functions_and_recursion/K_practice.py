# Write a resursive function to calculate the sum of first n natural numbers.

def sum_num(n):
    if n == 0:
        return 0
    return n + sum_num(n - 1)

print(sum_num(3))