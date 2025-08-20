# Problem: Odd or Even Vehicle Traffic Rule Checker

# Goal:
# To reduce traffic in particular areas, the city has introduced a rule:
# - Vehicles with EVEN last digit can drive only on Monday, Wednesday, Friday.
# - Vehicles with ODD last digit can drive only on Tuesday, Thursday, Saturday.
# - On Sunday, ALL vehicles are allowed.


special_day = "Sunday"
days1= ["Monday","Wednesday","Friday"]
days2=["Tuesday","Thursday","Saturday"]

def allowed_orNot(day,num):
    last_digit = int(num[-1])
    if day == "Sunday":
        print("Every vehicle is allowed on sunday")
    elif last_digit %2 == 0 and day in days1:
        print(f"The vehicle with the number {num} is allowed to drive on {day}")
    elif last_digit %2 != 0 and day in days2:
        print(f"The vehicle with the number {num} is allowed to drive on {day}")

    else:
        print(f"The vehicle with the number {num} is not alloweded to drive on {day}\n - try other days")

def check_day(num):
    day =input("Enter day of week: ")
    days = str(day).capitalize()
    if days not in days1 and days not in days2 and days not in special_day:
        print("Please enter a valid day")
        return check_day(num)
    else:
        allowed_orNot(days,num)

def check_number():
    vehicle_no = input("\nEnter your vehicle number(only Number not the region code): ")
    no_vehicle = int(vehicle_no)
    if len(vehicle_no) != 4:
        print("Length of vehicle number should be 4 digits")
        check_number()

    else:
        check_day(vehicle_no)
check_number()




