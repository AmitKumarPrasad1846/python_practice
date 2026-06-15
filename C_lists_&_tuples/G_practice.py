# WAP to count the number of students with the "A" grade in the following tuple.
# ["C", "D", "A", "A", "B", "B", "A"]
# Store the above values in a list & sort them from "A" to "D".

my_list = ["C", "D", "A", "A", "B", "B", "A"]

count = my_list.count("A")
print(count)

my_list_2 = my_list.copy()
sort = my_list_2.sort()
print(my_list_2)