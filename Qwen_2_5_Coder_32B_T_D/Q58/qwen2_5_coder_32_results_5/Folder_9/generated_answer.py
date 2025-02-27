import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    m, n = matrix.shape
    for i in range(m - 33 + 1):
        for j in range(n - 33 + 1):
            if matrix[i:i + 34, j:j + 34].size == 33:
                count += 1
    return count