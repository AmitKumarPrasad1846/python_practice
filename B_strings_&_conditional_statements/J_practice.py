# WAP to find the greatest of 3 numbers entered by the user.

num1 = int(input("enter the first no. :"))
num2 = int(input("enter the second no. :"))
num3 = int(input("enter the third no. :"))

if (num1>num2 and num1>num3):
    print(num1, "is the largest no.")
elif (num2>num3):
    print(num2, "is the largest no.")
else:
    print(num3, "is the largest no.")