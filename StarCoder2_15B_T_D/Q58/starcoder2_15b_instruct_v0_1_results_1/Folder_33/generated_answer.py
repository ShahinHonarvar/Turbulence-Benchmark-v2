import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 118
    row_count, col_count = matrix.shape
    submatrix_count = 0
    for row_start in range(row_count - n + 1):
        for col_start in range(col_count - n + 1):
            submatrix = matrix[row_start:row_start + n, col_start:col_start + n]
            if np.sum(submatrix) == n:
                submatrix_count += 1
    return submatrix_count