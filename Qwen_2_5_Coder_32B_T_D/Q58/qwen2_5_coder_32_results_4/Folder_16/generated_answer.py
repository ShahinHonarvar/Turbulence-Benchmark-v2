import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    m, n = matrix.shape
    for i in range(m - 143):
        for j in range(n - 143):
            if np.sum(matrix[i:i + 154, j:j + 154]) == 154:
                count += 1
    return count