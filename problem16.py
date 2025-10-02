# 16.Find longest word in a sentence

a = "Taj mahal is one of the seven wonders in the world"
splited_a = a.split()
longest = ""
for x in splited_a:
    if len(x) > len(longest):
        longest = x
print(longest)

#python shortcut
long = max(a.split(),key=len)
print("Longest word:",long)