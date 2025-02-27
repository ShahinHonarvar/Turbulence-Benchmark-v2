import numpy as np

def submatrix_with_n_numbers(matrix):
    num_rows, num_cols = matrix.shape
    count = 0
    for row_start in range(num_rows - 2):
        for col_start in range(num_cols - 2):
            submatrix = matrix[row_start:row_start + 3, col_start:col_start + 3]
            if np.sum(submatrix) == 59:
                count += 1
    return count