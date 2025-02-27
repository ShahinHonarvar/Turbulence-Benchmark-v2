import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    rows, cols = matrix.shape
    m, n = (rows, cols)
    for i in range(m):
        for j in range(n):
            for size in range(1, min(m - i + 1, n - j + 1) + 1):
                submatrix = matrix[i:i + size, j:j + size]
                if submatrix.sum() == -42:
                    result.append(submatrix)
    return result