import numpy as np

def submatrix_with_n_numbers(matrix):
    if not isinstance(matrix, np.ndarray) or matrix.ndim != 2:
        raise ValueError('Input must be a 2D numpy matrix')
    n_rows, n_cols = matrix.shape
    submatrix_count = 0
    for size in range(1, n_rows + 1):
        for i in range(n_rows - size + 1):
            for j in range(n_cols - size + 1):
                submatrix = matrix[i:i + size, j:j + size]
                if submatrix.size == 144:
                    submatrix_count += 1
    return submatrix_count