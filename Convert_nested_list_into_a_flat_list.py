nested = [[1, 2], [3, 4], [5, 6]]
flat = []
for group in nested:
    for item in group:
        flat.append(item)
print(flat)
