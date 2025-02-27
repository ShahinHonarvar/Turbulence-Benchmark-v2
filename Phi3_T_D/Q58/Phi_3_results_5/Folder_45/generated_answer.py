import numpy as np

def submatrix_with_n_numbers(matrix):
    if not isinstance(matrix, np.ndarray) or len(matrix.shape) != 2:
        return 0
    count = 0
    nrows, ncols = matrix.shape
    size = 28
    for row_start in range(nrows):
        for col_start in range(ncols):
            if row_start + size <= nrows and col_start + size <= ncols:
                count += 1
    return count