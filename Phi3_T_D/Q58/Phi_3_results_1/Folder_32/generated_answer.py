import numpy as np

def submatrix_with_n_numbers(matrix):
    if not isinstance(matrix, np.ndarray):
        raise ValueError('Input matrix should be a numpy array')
    if matrix.ndim != 2:
        raise ValueError('Input matrix should be two-dimensional')
    m, n = matrix.shape
    count = 0
    for i in range(m):
        for j in range(n):
            if matrix[i, j] == 103:
                count += 1
    return count