import numpy as np

def submatrix_with_particular_sum(matrix):
    m, n = matrix.shape
    result = []
    for size in range(1, min(m, n) + 1):
        for row in range(m - size + 1):
            for col in range(n - size + 1):
                sub_matrix = matrix[row:row + size, col:col + size]
                if sub_matrix.sum() == 38:
                    result.append(sub_matrix)
    return result