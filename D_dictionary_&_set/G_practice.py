"""
WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with an empty dictionary & add one by one. Use subject name as key & marks as value.
"""

# subject_mark = {}
# subject_mark["maths"] = int(input("enter your maths marks : "))
# subject_mark["chem"] = int(input("enter your chemistry marks : "))
# subject_mark["BEEE"] = int(input("enter your BEEE marks : "))

# print(subject_mark)

# ================OR=================

mark = {}
x = int(input('Enter your maths marks : '))
mark.update({"maths": x})

y = int(input('Enter your chem marks : '))
mark.update({"chem": y})

z = int(input('Enter your BEEE marks : '))
mark.update({"BEEE" : z})

print(mark)