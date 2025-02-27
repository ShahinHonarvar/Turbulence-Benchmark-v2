import numpy as np

def submatrix_with_n_numbers(matrix):
    num_rows, num_cols = matrix.shape
    num_submatrices = 0
    for row_start in range(num_rows - 3):
        for col_start in range(num_cols - 3):
            submatrix = matrix[row_start:row_start + 4, col_start:col_start + 4]
            num_submatrices += 1 if submatrix.size == 18 else 0
    return num_submatrices