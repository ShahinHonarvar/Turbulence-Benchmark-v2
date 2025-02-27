import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    m, n = matrix.shape
    for i in range(m - 8):
        for j in range(n - 8):
            if np.sum(matrix[i:i + 9, j:j + 9] == 95) == 81:
                count += 1
    return count