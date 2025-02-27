import numpy as np

def submatrix_with_n_numbers(matrix):
    m, n = matrix.shape
    count = 0
    for i in range(m - 13):
        for j in range(n - 13):
            if np.sum(matrix[i:i + 14, j:j + 14]) == 147:
                count += 1
    return count