import numpy as np

def submatrix_with_particular_sum(matrix):
    n_rows, n_cols = matrix.shape
    submatrices = []
    for left_col in range(n_cols):
        for right_col in range(left_col, n_cols):
            for top_row in range(n_rows):
                for bottom_row in range(top_row, n_rows):
                    submatrix = matrix[top_row:bottom_row + 1, left_col:right_col + 1]
                    if np.sum(submatrix) == -10:
                        submatrices.append(submatrix)
    return submatrices