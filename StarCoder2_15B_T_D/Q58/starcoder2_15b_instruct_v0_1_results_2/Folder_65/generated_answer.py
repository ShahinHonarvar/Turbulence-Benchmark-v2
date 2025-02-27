import numpy as np

def submatrix_with_n_numbers(matrix):
    if not isinstance(matrix, np.ndarray) or matrix.ndim != 2:
        raise ValueError('Invalid matrix: must be a 2D numpy array')
    num_rows, num_cols = matrix.shape
    num_numbers_per_submatrix = 35
    submatrix_size = int(np.sqrt(num_numbers_per_submatrix))
    num_submatrices = 0
    for i in range(num_rows - submatrix_size + 1):
        for j in range(num_cols - submatrix_size + 1):
            submatrix = matrix[i:i + submatrix_size, j:j + submatrix_size]
            if np.sum(submatrix) == num_numbers_per_submatrix:
                num_submatrices += 1
    return num_submatrices