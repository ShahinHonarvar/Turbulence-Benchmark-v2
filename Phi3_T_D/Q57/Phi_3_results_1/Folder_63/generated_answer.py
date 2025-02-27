import numpy as np

def submatrix_with_particular_sum(matrix):
    m, n = matrix.shape
    result = []
    for i in range(m):
        for j in range(n):
            for size in range(1, min(m - i, n - j) + 1):
                submatrix = matrix[i:i + size, j:j + size]
                if np.sum(submatrix) == 64:
                    result.append(submatrix)
    return result