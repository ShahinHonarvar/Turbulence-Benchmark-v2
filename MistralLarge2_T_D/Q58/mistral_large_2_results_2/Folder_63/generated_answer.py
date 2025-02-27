import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for top_row in range(rows):
        for bottom_row in range(top_row, rows):
            for left_col in range(cols):
                for right_col in range(left_col, cols):
                    submatrix = matrix[top_row:bottom_row + 1, left_col:right_col + 1]
                    if submatrix.size == 57:
                        count += 1
    return count