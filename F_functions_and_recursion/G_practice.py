# WAF to convert USD to INR

# def convert(n):
#     inr = 94.3
#     print(f"{n} $ is total {inr*n} Rs")

# convert(5)

# ==========================================================

def convert():
    n = float(input("How many dollors you want ot convert? :"))
    inr = float(input("What's the current inr value? :"))
    print(f"{n} $ is total {inr*n} Rs")

convert()