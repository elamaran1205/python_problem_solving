# 18. Factorial – n! using loop or recursion.

def get_fact_value(num):
    factvalue = 1
    for x in range(1,num+1):
        factvalue *= x
    print(f"Factorial of {num} is {factvalue}")

def get_value():
    a = int(input("Enter a number: "))
    if a <0 :
        print("Enter a valid number !")
        get_value()
    elif(a == 0):
        print(f"Factorial of {a} is 1")
    else:
        get_fact_value(a)

get_value()
