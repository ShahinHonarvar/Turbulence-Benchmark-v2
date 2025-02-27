import numpy as np

def submatrix_with_n_numbers(matrix):
    m, n = matrix.shape
    if m * n < 173:
        return 0
    count = 0
    for i in range(m - 13):
        for j in range(n - 13):
            if np.unique(matrix[i:i + 13, j:j + 13]).size == 173:
                count += 1
    return count