# WAP to check if a list contains a palindrome of elements. (Hint: use copy() method)
# palindrome element example : [1, 2, 3, 2, 1] , [1, "abc", "abc", 1]

# my_list = []
# i = int(input("whats the total word count of the list? = "))
# for j in range(1, i+1):
#     list_ele = input(f"input the list {j} element")
#     my_list.append(list_ele)

# rev_list = my_list.copy()
# rev_list.reverse()

# if my_list == rev_list:
#     print(my_list, "is palindrome")
# else:
#     print(my_list, "is not palindrome")

my_list = [1, 2, 3, 4, 5]
dup_list = my_list.copy()
dup_list.reverse()

if my_list==dup_list:
    print("your list is palindrome.")
else:
    print("not palindrome.")