# Search for a numbers x in this tuple using for loop:
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

tup = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x = int(input("enter a number to find : "))

idx = 0
for char in tup:
    if char == x:
        print(f"{x} is found at {idx}")
        break
    idx += 1
else:
    print(f"{x} is not found in the data")