# 8.Find the missing number in a sequence.

a = [2,2,3,5,6,7]
n=7

missing = set(range(2,n+1))-set(a)
# {2,3,4,5,6,7} - {2,3,5,6,7} = {4}
print(missing) #4