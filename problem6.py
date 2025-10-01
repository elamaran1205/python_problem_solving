# Check if a list is palindrome.

alist = [1,2,3,3,2,1]

if(alist == alist[::-1]):
    print("Palindrome")
else:
    print("Not a Palindrome")