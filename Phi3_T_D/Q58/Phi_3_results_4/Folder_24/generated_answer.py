import numpy as np

def submatrix_with_n_numbers(matrix):
    if not isinstance(matrix, np.ndarray) or matrix.ndim != 2:
        return 0
    n_rows, n_cols = matrix.shape
    count = 0
    for i in range(n_rows):
        for j in range(n_cols):
            if i + 50 < n_rows and j + 50 < n_cols:
                submatrix_size = 51
                submatrix = matrix[i:i + submatrix_size, j:j + submatrix_size]
                if np.all(submatrix == 51):
                    count += 1
    return count