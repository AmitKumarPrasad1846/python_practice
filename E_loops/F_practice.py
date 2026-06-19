# Search for a numbers x in this tuple using while loop:
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 10]

data = (1, 4, 9, 16, 25, 36, 49, 64, 81, 10)

x = int(input("Which number you wanna check? = "))
idx = 0
while idx < len(data) + 1:
    if data[idx] == x:
        print(f"Number found at {idx}")
    idx+=1

