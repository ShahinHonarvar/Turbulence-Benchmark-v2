import numpy as np

def submatrix_with_particular_sum(matrix):
    rows_, cols_ = matrix.shape
    results = []
    for top_row in range(rows_):
        for bottom_row in range(top_row, rows_):
            for left_col in range(cols_):
                for right_col in range(left_col, cols_):
                    submatrix = matrix[top_row:bottom_row + 1, left_col:right_col + 1]
                    if np.sum(submatrix) == -6:
                        results.append(submatrix)
    return results