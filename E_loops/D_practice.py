# Print the multiplication table of a number n.

n = int(input("Which table you wanna print ? = "))
i = 1
while i <=10:
    x = i * n
    print(f"{n} X {i} = {x}")
    i+=1

print(f"Here is your table of {n}")