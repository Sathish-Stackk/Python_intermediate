words = ["apple", "ant", "banana", "ball", "cat"]
groups = {}
for word in words:
    key = word[0]
    groups.setdefault(key, []).append(word)
print(groups)
