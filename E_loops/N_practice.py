# Print the multiplication table of a number n.

n = int(input("Which table you want? = "))

for i in range (1, 11):
    print(f"{n} X {i} = {n*i}")

print("table print successfull !!")