import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    n = len(matrix)
    m = len(matrix[0])

    def check_sum(submatrix):
        return np.sum(submatrix) == 54

    def add_submatrix(x, y, width, height, level, submatrix):
        submatrix_data = matrix[x:x + width, y:y + height]
        if check_sum(submatrix_data):
            result.append(submatrix_data.tolist())
        if width > 1:
            add_submatrix(x, y, width - 1, height, level + 1, submatrix_data.tolist())
        if height > 1:
            add_submatrix(x + 1, y, width, height - 1, level + 1, submatrix_data.tolist())
    for i in range(n):
        for j in range(m):
            add_submatrix(i, j, n - i, m - j, 0, np.array([[]]))
    return result