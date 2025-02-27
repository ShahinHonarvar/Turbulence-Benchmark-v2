import numpy as np

def submatrix_with_n_numbers(matrix):
    m, n = matrix.shape
    count = 0
    for i in range(m - 8):
        for j in range(n - 8):
            if np.sum(matrix[i:i + 9, j:j + 9] == 93) == 81:
                count += 1
    return count