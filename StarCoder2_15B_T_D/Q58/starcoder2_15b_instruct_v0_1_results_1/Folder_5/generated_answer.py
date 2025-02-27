import numpy as np

def submatrix_with_n_numbers(matrix):
    if not isinstance(matrix, np.ndarray) or matrix.ndim != 2 or (not matrix.dtype == int):
        raise TypeError('Invalid matrix: must be a two-dimensional numpy array of integers')
    m, n = matrix.shape
    count = 0
    for i in range(m - 2):
        for j in range(n - 2):
            submatrix = matrix[i:i + 3, j:j + 3]
            if submatrix.size == 63:
                count += 1
    return count