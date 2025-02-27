import numpy as np

def submatrix_with_n_numbers(matrix):
    if not isinstance(matrix, np.ndarray) or not len(matrix.shape) == 2:
        return 0
    submatrix_count = 0
    rows, cols = matrix.shape
    for row_start in range(rows):
        for col_start in range(cols):
            for row_len in range(1, rows - row_start + 1):
                for col_len in range(1, cols - col_start + 1):
                    if row_len * col_len == 63:
                        submatrix_count += 1
    return submatrix_count