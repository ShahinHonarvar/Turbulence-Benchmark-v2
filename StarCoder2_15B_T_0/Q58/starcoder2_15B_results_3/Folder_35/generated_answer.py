import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 111
    m, n = matrix.shape
    count = 0
    for i in range(m - n + 1):
        for j in range(n - n + 1):
            submatrix = matrix[i:i + n, j:j + n]
            if np.sum(submatrix) == n:
                count += 1
    return count