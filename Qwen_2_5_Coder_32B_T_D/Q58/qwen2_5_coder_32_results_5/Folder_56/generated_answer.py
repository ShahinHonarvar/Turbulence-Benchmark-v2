import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    m, n = matrix.shape
    for i in range(m - 7):
        for j in range(n - 7):
            if np.sum(matrix[i:i + 8, j:j + 8]) == 68:
                count += 1
    return count