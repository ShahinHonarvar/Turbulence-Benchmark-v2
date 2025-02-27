import numpy as np

def submatrix_with_n_numbers(matrix):
    n_rows, n_cols = matrix.shape
    count = 0
    for row_start in range(n_rows - 2):
        for col_start in range(n_cols - 2):
            submatrix = matrix[row_start:row_start + 3, col_start:col_start + 3]
            if submatrix.size == 121:
                count += 1
    return count