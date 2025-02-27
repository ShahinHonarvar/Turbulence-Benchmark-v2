import numpy as np

def submatrix_with_n_numbers(matrix):
    if not isinstance(matrix, np.ndarray) or matrix.ndim != 2:
        raise ValueError('Input must be a two-dimensional numpy array')
    n_rows, n_cols = matrix.shape
    n_numbers = 54
    count = 0
    for i in range(n_rows - 2):
        for j in range(n_cols - 2):
            submatrix = matrix[i:i + 3, j:j + 3]
            if np.sum(submatrix == n_numbers):
                count += 1
    return count