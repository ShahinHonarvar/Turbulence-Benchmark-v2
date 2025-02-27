import numpy as np

def submatrix_with_n_numbers(matrix):
    num_rows, num_cols = matrix.shape
    num_submatrices = 0
    for row_start in range(num_rows - 130):
        for col_start in range(num_cols - 130):
            submatrix = matrix[row_start:row_start + 131, col_start:col_start + 131]
            num_elements = np.count_nonzero(~np.isnan(submatrix))
            if num_elements == 131:
                num_submatrices += 1
    return num_submatrices