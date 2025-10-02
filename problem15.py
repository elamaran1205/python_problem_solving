# 15.Remove duplicates from a string

# method 1
a = "aabbccddd"
cleaned_a = set(sorted(a))
print(cleaned_a)

# method 2
b = "allaballa"
cleaned_b = ""
for x in b:
    if x not in cleaned_b:
        cleaned_b +=x
print(cleaned_b)