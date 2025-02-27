import numpy as np

def submatrix_with_n_numbers(matrix):
    n_rows, n_cols = matrix.shape
    count = 0
    for row_start in range(n_rows - 4):
        for col_start in range(n_cols - 4):
            submatrix = matrix[row_start:row_start + 5, col_start:col_start + 5]
            if np.sum(submatrix) == 23:
                count += 1
    return count