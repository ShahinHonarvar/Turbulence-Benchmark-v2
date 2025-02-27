import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for top_row in range(rows):
        for left_col in range(cols):
            for bottom_row in range(top_row + 1, rows + 1):
                for right_col in range(left_col + 1, cols + 1):
                    submatrix = matrix[top_row:bottom_row, left_col:right_col]
                    if np.prod(submatrix.shape) == 42:
                        count += 1
    return count