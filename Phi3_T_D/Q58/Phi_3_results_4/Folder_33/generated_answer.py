import numpy as np

def submatrix_with_n_numbers(matrix):
    if not isinstance(matrix, np.ndarray):
        raise ValueError('Input must be a NumPy matrix')
    if matrix.ndim != 2:
        raise ValueError('Input must be a 2-dimensional matrix')
    count = 0
    rows, cols = matrix.shape
    for row_start in range(rows):
        for col_start in range(cols):
            for submatrix_rows in range(1, rows - row_start + 1):
                for submatrix_cols in range(1, cols - col_start + 1):
                    if submatrix_rows * submatrix_cols == 118:
                        submatrix = matrix[row_start:row_start + submatrix_rows, col_start:col_start + submatrix_cols]
                        count += 1
    return count