def rotate_matrix(matrix):
    return [list(row) for row in zip(*matrix[::-1])]

print(rotate_matrix([[1, 2], [3, 4]]))
