import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    m, n = matrix.shape
    for i in range(m - 4):
        for j in range(n - 4):
            if np.sum(matrix[i:i + 5, j:j + 5]) == 54:
                count += 1
    return count