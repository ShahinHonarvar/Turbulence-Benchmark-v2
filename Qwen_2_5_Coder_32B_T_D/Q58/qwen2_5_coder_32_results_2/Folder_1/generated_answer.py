import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    m, n = matrix.shape
    for i in range(m - 22):
        for j in range(n - 22):
            if matrix[i:i + 23, j:j + 23].size == 23:
                count += 1
    return count