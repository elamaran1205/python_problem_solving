# 11.Count vowels and consonants

a = "what is in the box"
vowels = ""
consonants = ""
for i in a:
    if i.lower() in "aeiou":
        vowels += i
    elif i.isalpha():
        consonants += i

print(f"vowels : {len(vowels)}")
print(f"consonants: {len(consonants)}")