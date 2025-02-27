import numpy as np

def submatrix_with_n_numbers(matrix):
    if not isinstance(matrix, np.ndarray) or matrix.ndim != 2:
        raise ValueError('The input matrix must be a two-dimensional numpy array.')
    n_rows, n_cols = matrix.shape
    submatrix_size = 45
    count = 0
    for i in range(n_rows - submatrix_size + 1):
        for j in range(n_cols - submatrix_size + 1):
            submatrix = matrix[i:i + submatrix_size, j:j + submatrix_size]
            if submatrix.size == submatrix_size:
                count += 1
    return count