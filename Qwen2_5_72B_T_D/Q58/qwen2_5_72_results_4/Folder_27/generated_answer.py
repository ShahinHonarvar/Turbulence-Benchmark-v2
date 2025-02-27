import numpy as np

def submatrix_with_n_numbers(matrix):
    target_count = 77
    rows, cols = matrix.shape
    valid_submatrices = 0
    for row_start in range(rows):
        for col_start in range(cols):
            for row_end in range(row_start, rows):
                for col_end in range(col_start, cols):
                    if np.sum(matrix[row_start:row_end + 1, col_start:col_end + 1] == target_count) == target_count:
                        valid_submatrices += 1
    return valid_submatrices