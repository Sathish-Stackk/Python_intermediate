a = [1, 2, 3, 4, 5]
b = [2, 3, 5, 7]
c = [2, 5, 8]
result = set(a) & set(b) & set(c)
print("Common:", sorted(result))
