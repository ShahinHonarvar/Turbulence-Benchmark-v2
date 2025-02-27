import numpy as np

def submatrix_with_n_numbers(matrix):
    m, n = matrix.shape
    count = 0
    for i in range(m - 75):
        for j in range(n - 75):
            submatrix = matrix[i:i + 76, j:j + 76]
            if np.sum(submatrix) == 76 * 76:
                count += 1
    return count