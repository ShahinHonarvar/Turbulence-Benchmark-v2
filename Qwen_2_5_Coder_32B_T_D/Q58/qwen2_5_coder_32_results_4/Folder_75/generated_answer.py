import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    m, n = matrix.shape
    for i in range(m - 7):
        for j in range(n - 7):
            if np.size(matrix[i:i + 8, j:j + 8]) == 80:
                count += 1
    return count