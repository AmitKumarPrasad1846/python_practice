# HW question
# WAF to for printing even and odd number.

def number():
    n = int(input("enter a number : "))
    if n%2==0:
        print(f"{n} is an even number.")
    else:
        print(f"{n} is an odd number.")

number()