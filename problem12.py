# 12.Count frequency of characters

a = "Franccefe"
count = {}
print(count)

for i in a:
    count[i] = count.get(i,0)+1

print(count)