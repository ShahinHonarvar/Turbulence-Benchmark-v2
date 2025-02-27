import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    m, n = matrix.shape
    for i in range(m - 5, -1, -1):
        for j in range(n - 5, -1, -1):
            if np.sum(matrix[i:i + 6, j:j + 6]) == 39:
                count += 1
    return count