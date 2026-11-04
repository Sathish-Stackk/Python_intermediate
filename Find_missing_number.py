numbers = [1, 2, 3, 5, 6, 7]
n = 7

expected = n * (n + 1) // 2
actual = sum(numbers)

missing = expected - actual

print("Missing Number:", missing)
