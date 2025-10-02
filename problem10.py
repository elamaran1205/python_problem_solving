# 10.Check if string is palindrome

a = "madam"
isPalindrome = True
length = len(a)
for i in range(length//2):
    if a[i] != a[length-1-i]:
    #a[o] != a[5-1-0] - first loop - a[0] != a[4] - m == m
    #a[1] != a[5-1-1] - second loop - a[1] != a[3] - a == a
        isPalindrome = False
        break

if isPalindrome:
    print("Palindrome")
else:
    print("Not a Palindrome")