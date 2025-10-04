# 20.Armstrong number – sum of powered digits equals number.
def armstrong(n):
    n_length = len(str(n))
    total = 0
    loopn = n   
    while loopn>0:
        digit = loopn%10
        total += digit**n_length
        loopn //=10
    return total == n

a = int(input("Enter a number to check:"))  

if armstrong(a):
    print(f"{a} It is Armstrong numner")
else:
    print(f"{a} it is not a Armstrong number")