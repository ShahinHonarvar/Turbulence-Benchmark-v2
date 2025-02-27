import numpy as np

def submatrix_with_n_numbers(matrix):
    num_rows, num_cols = matrix.shape
    num_numbers = 83
    submatrix_count = 0
    for row_start in range(num_rows - 1):
        for col_start in range(num_cols - 1):
            submatrix = matrix[row_start:row_start + 2, col_start:col_start + 2]
            num_submatrix_numbers = np.count_nonzero(~np.isnan(submatrix))
            if num_submatrix_numbers == num_numbers:
                submatrix_count += 1
    return submatrix_count