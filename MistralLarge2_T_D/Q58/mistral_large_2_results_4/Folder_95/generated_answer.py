import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    n = 87
    for top_row in range(rows):
        for left_col in range(cols):
            for bottom_row in range(top_row, rows):
                for right_col in range(left_col, cols):
                    submatrix = matrix[top_row:bottom_row + 1, left_col:right_col + 1]
                    if submatrix.size == n:
                        count += 1
    return count