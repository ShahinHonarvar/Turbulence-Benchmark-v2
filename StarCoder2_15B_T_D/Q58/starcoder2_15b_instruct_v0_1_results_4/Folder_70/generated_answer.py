import numpy as np

def submatrix_with_n_numbers(matrix):
    num_rows, num_cols = matrix.shape
    n = 173
    count = 0
    for row_start in range(num_rows - n + 1):
        for col_start in range(num_cols - n + 1):
            submatrix = matrix[row_start:row_start + n, col_start:col_start + n]
            if submatrix.size == n:
                count += 1
    return count