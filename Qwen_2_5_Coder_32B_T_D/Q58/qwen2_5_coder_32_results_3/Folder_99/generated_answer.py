import numpy as np

def submatrix_with_n_numbers(matrix):
    m, n = matrix.shape
    count = 0
    for i in range(m - 13 + 1):
        for j in range(n - 13 + 1):
            if np.sum(matrix[i:i + 13, j:j + 13]) == 146:
                count += 1
    return count