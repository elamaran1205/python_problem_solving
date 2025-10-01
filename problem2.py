# Find second largest element.

alist = [843,434,454,345]
print(sorted(alist)[-2])

alist.sort(reverse=True)
print(alist[1])