import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    submatrices = []
    for top_row in range(rows):
        for left_col in range(cols):
            for bottom_row in range(top_row, rows):
                for right_col in range(left_col, cols):
                    submatrix = matrix[top_row:bottom_row + 1, left_col:right_col + 1]
                    if np.sum(submatrix) == 38:
                        submatrices.append(submatrix)
    return submatrices