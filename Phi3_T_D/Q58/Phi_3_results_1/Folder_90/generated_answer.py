import numpy as np

def submatrix_with_n_numbers(matrix):
    if not isinstance(matrix, np.ndarray):
        raise ValueError('Input must be a numpy matrix')
    if matrix.ndim != 2:
        raise ValueError('Matrix must be two-dimensional')
    rows, cols = matrix.shape
    count = 0
    for row_start in range(rows):
        for col_start in range(cols):
            for row_len in range(1, rows - row_start + 1):
                for col_len in range(1, cols - col_start + 1):
                    submatrix = matrix[row_start:row_start + row_len, col_start:col_start + col_len]
                    if submatrix.size == 176:
                        count += 1
    return count