import numpy as np

def submatrix_with_n_numbers(matrix):
    num_rows, num_cols = matrix.shape
    count = 0
    for row_start in range(num_rows - 1):
        for col_start in range(num_cols - 1):
            submatrix = matrix[row_start:row_start + 2, col_start:col_start + 2]
            if np.sum(submatrix) == 46:
                count += 1
    return count