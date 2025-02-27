import numpy as np

def submatrix_with_n_numbers(matrix):
    if not isinstance(matrix, np.ndarray):
        raise ValueError('Input must be a numpy ndarray.')
    if matrix.ndim != 2:
        raise ValueError('Input must be a two-dimensional numpy matrix.')
    count = 0
    num_rows, num_cols = matrix.shape
    for row_start in range(num_rows):
        for col_start in range(num_cols):
            for row_len in range(1, num_rows - row_start + 1):
                for col_len in range(1, num_cols - col_start + 1):
                    if row_len * col_len == 27:
                        submatrix = matrix[row_start:row_start + row_len, col_start:col_start + col_len]
                        if np.all(submatrix == 0):
                            count += 1
    return count