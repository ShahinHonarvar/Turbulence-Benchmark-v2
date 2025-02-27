import numpy as np

def submatrix_with_n_numbers(matrix):
    m, n = matrix.shape
    count = 0
    for i in range(m - 5):
        for j in range(n - 5):
            submatrix = matrix[i:i + 6, j:j + 6]
            if np.size(submatrix) == 39:
                count += 1
    return count