import sys
cart = {}
print("Welcome to LMN shopping cart section")

def total_amount():
    for itemm,prices in cart.items():
        print(f"{itemm} - ₹{prices}")
    total = sum(cart.values())
    large = max(cart,key=cart.get)
    print(f"Highest amount item : {large} - Price(₹{cart[large]})")
    sys,exit(f"Total Amount : {total}")


def add_items():
    global cart
    items = input("Enter the item name:")
    price = int(input("Enter the price of the item without currency symbol:"))
    cart[items] = price
    for itemm,prices in cart.items():
         print(f"{itemm} - ₹{prices}")
         check=int(input("To see cart press 1 | Skip? Press 0 to continue:"))
         if check == 1:
             total_amount()
         elif check == 0:
            check_input()
         else:
             print("Invalid input")
             check_input()
                     
                
def check_input():
        value = (int(input("Press 1 to add items in cart and 0 to exit:")))
        if value in [1,0]:
            if value == 1:
                add_items()
            elif value == 0:
                sys.exit("Exited .")
            else:
                print("something wrong try again")
        else:
            print("Enter a valid input")
            return check_input()

check_input()