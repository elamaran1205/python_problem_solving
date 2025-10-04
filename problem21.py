# 21.Sum of digits – break a number and add digits.

a = 3425763
total = 0
for digit in str(a):
    total += int(digit)

print(total)