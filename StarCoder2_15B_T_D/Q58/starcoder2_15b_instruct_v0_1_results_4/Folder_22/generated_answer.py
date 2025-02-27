import numpy as np

def submatrix_with_n_numbers(matrix):
    num_rows, num_cols = matrix.shape
    result = 0
    for row_start in range(num_rows - 4):
        for col_start in range(num_cols - 4):
            submatrix = matrix[row_start:row_start + 5, col_start:col_start + 5]
            if np.sum(submatrix) == 21:
                result += 1
    return result