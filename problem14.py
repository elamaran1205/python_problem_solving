# 14.Find the first non-repeated character

a = "eeeeddddcccfvvvggg"
count = {}

for i in a:
    count[i] = count.get(i,0)+1

for x in a:
    if count[x] == 1:
        print("non-repeated character",x)
