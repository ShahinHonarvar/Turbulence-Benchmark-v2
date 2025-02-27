import numpy as np

def submatrix_with_n_numbers(matrix):
    total_rows, total_cols = matrix.shape
    target_size = 120
    valid_submatrices = 0
    for row_start in range(total_rows):
        for col_start in range(total_cols):
            for row_end in range(row_start + 1, total_rows + 1):
                for col_end in range(col_start + 1, total_cols + 1):
                    submatrix = matrix[row_start:row_end, col_start:col_end]
                    if submatrix.size == target_size:
                        valid_submatrices += 1
    return valid_submatrices