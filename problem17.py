# Prime number check – is a number prime or not ?


def checkprime(num):
    is_prime =True
    if num <= 1:
        print("It's not a prime")
    else:
        for i in range(2,num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(f"The number {num} is prime")
        else:
            print(f"The number {num} is not a prime")

a= int(input("Enter a number : "))
checkprime(a)