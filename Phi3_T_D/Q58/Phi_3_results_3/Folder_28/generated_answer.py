import numpy as np

def submatrix_with_n_numbers(matrix, n=37):
    rows, cols = matrix.shape
    count = 0
    for row_top in range(rows):
        for row_bottom in range(row_top, rows):
            submatrix_rows = row_bottom - row_top + 1
            for col_left in range(cols):
                for col_right in range(col_left, cols):
                    submatrix_cols = col_right - col_left + 1
                    if submatrix_rows * submatrix_cols == n:
                        count += 1
    return count