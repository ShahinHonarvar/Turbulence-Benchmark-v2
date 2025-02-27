import numpy as np

def submatrix_with_n_numbers(matrix):
    if not isinstance(matrix, np.ndarray) or matrix.ndim != 2:
        raise ValueError('Input must be a two-dimensional numpy array.')
    num_rows, num_cols = matrix.shape
    n = 87
    count = 0
    for i in range(num_rows - n + 1):
        for j in range(num_cols - n + 1):
            submatrix = matrix[i:i + n, j:j + n]
            if submatrix.size == n:
                count += 1
    return count