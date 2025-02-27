import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    m, n = matrix.shape
    for i in range(m - 11 + 1):
        for j in range(n - 11 + 1):
            if np.sum(matrix[i:i + 11, j:j + 11]) == 127:
                count += 1
    return count