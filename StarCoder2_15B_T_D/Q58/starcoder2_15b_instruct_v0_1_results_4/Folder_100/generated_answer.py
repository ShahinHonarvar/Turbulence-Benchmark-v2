import numpy as np

def submatrix_with_n_numbers(matrix):
    row_count, col_count = matrix.shape
    submatrix_count = 0
    for row_start in range(row_count - 1):
        for col_start in range(col_count - 1):
            submatrix = matrix[row_start:row_start + 2, col_start:col_start + 2]
            if np.count_nonzero(submatrix) == 10:
                submatrix_count += 1
    return submatrix_count