# Write a recursive function to print all elements in a list.
# Hint : use list and index as parameters.

def print_li(list, index=0):
    if (index == len(list)):
        return
    print(list[index])
    print_li(list, index+1)

cars = ["buggati", "Rolls royce", "pagani", "BMW", "MC laren"]
print_li(cars)