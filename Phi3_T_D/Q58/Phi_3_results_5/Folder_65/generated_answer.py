import numpy as np

def submatrix_with_n_numbers(matrix):
    if matrix.ndim != 2:
        return 0
    nrows, ncols = matrix.shape
    count = 0
    n = 35
    for row_top in range(nrows):
        for col_left in range(ncols):
            for row_bottom in range(row_top, nrows):
                for col_right in range(col_left, ncols):
                    submatrix_size = (row_bottom - row_top + 1) * (col_right - col_left + 1)
                    if submatrix_size == n:
                        count += 1
    return count