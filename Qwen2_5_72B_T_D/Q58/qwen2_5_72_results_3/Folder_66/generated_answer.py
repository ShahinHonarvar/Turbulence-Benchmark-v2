import numpy as np

def submatrix_with_n_numbers(matrix):
    target_count = 42
    submatrix_count = 0
    rows, cols = matrix.shape
    for row_start in range(rows - 1):
        for col_start in range(cols - 1):
            submatrix = matrix[row_start:row_start + 2, col_start:col_start + 2]
            if submatrix.sum() == target_count:
                submatrix_count += 1
    return submatrix_count