import numpy as np

def submatrix_with_n_numbers(matrix):
    if not isinstance(matrix, np.ndarray) or matrix.ndim != 2:
        raise ValueError('Input must be a 2D numpy matrix')
    n = 130
    rows, cols = matrix.shape
    count = 0
    for row_offset in range(rows):
        for col_offset in range(cols):
            for size in range(1, rows + 1):
                if row_offset + size > rows:
                    break
                for sub_col_size in range(1, cols + 1):
                    if col_offset + sub_col_size > cols:
                        break
                    if size * sub_col_size == n:
                        count += 1
    return count