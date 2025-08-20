# Classic FizzBuzz but with a traffic-rule theme (to keep it fun).

number = input("Enter a number : ")
num = int(number)
for x in range(1,num+1):
    if x %3 == 0 and x %5 == 0:
        print("Road Block")
    elif x %3 == 0 :
        print("Checkpoint")
    elif x %5 == 0:
        print("Traffic Jam")
    else:
        print(x)