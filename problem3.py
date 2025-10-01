# Remove duplicates
arrvalue = [2,34,3,25,3,25,123,54,35,123,3]


#using loops
newarrvalue = [] 
for x in arrvalue:
    if x not in newarrvalue:
        newarrvalue.append(x)
print(newarrvalue)

#using set
cleaned_version = set(arrvalue)
print(cleaned_version)