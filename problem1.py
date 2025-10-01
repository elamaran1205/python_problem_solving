# Find largest element in a list.
newlist = [12,423,452,623]

#using max
print(max(newlist))

#using loop
largest = newlist[0]
for x in newlist:
    if x > largest:
        largest = x

print(largest)

#using sort
print(sorted(newlist)[-1])
newlist.sort(reverse=True)
print(newlist[0])
