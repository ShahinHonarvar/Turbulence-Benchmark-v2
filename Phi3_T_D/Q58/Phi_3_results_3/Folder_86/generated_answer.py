import numpy as np

def submatrix_with_n_numbers(matrix):
    m, n = matrix.shape
    count = 0
    for i in range(m):
        for j in range(n):
            if matrix[i, j] == 138:
                size = min(m - i, n - j)
                if size > 0:
                    count += 1
    return count