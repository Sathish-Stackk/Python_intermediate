nums = [16, 17, 4, 3, 5, 2]
leaders = []
maximum = float("-inf")

for n in reversed(nums):
    if n > maximum:
        leaders.append(n)
        maximum = n

print("Leaders:", leaders[::-1])
