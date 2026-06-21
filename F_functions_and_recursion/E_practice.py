# Write a function to print the elements of a list in a single line. (list is the parameter)

subjects = ["maths", "chemistry", "physics", "Engineering drawing", "BEEE"]

# def pri_li(list):
#     print(subjects)

# pri_li(subjects)

def print_list(list):
    for i in list:
        print(i, end=" ")

print_list(subjects)
