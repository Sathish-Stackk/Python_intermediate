import math

nums = [4, 10, 16, 20, 25, 30, 36]
squares = []

for n in nums:
    root = math.isqrt(n)
    if root * root == n:
        squares.append(n)

print("Perfect Squares:", squares)
