# WAF to find the factorial of n. (n is the parameter)

# def facto(n):
#     result = 1
#     for i in range(1, (n+1)):
#         result *= i
#     print("the factorial of the numbers is : ",result)

# facto(5)

def facto():
    n = int(input("Enter a number : "))
    result = 1
    for i in range(1, (n+1)):
        result *= i
    print("the factorial of the numbers is : ",result)

facto()