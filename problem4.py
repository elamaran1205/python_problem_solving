# Count the frequency of elements.

arr = [1,2,3,2,4,1,1,3,4]
freq = {}
for nums in arr:
    freq[nums] = freq.get(nums,0) +1

print(freq)