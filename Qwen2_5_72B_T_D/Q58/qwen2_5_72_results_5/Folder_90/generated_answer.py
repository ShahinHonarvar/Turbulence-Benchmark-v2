import numpy as np

def submatrix_with_n_numbers(matrix):
    target_count = 176
    submatrix_count = 0
    rows, cols = matrix.shape
    for row_start in range(rows - 13):
        for col_start in range(cols - 13):
            submatrix = matrix[row_start:row_start + 14, col_start:col_start + 14]
            if np.size(submatrix) == target_count:
                submatrix_count += 1
    return submatrix_count