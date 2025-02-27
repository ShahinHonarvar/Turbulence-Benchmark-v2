import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for top_row in range(rows):
        for left_col in range(cols):
            for bottom_row in range(top_row, rows):
                for right_col in range(left_col, cols):
                    if (bottom_row - top_row + 1) * (right_col - left_col + 1) == 76:
                        count += 1
    return count