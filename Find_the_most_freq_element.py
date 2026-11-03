nums = [4, 2, 4, 3, 4, 2, 5]
freq = {}
for n in nums:
    freq[n] = freq.get(n, 0) + 1
result = max(freq, key=freq.get)
print("Most frequent:", result)
