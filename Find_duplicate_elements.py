nums = [1, 2, 3, 2, 4, 5, 3, 6]
duplicates = list({n for n in nums if nums.count(n) > 1})
print("Duplicates:", duplicates)
