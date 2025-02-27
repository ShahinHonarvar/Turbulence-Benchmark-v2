import numpy as np

def submatrix_with_n_numbers(matrix):
    n_rows, n_cols = matrix.shape
    count = 0
    for row_start in range(n_rows - 1):
        for col_start in range(n_cols - 1):
            for row_end in range(row_start + 1, n_rows):
                for col_end in range(col_start + 1, n_cols):
                    sub_matrix = matrix[row_start:row_end + 1, col_start:col_end + 1]
                    if np.sum(sub_matrix) == 63:
                        count += 1
    return count