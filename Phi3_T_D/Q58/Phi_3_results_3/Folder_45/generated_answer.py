import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 28
    rows, cols = matrix.shape
    count = 0
    for row_top in range(rows):
        for row_bottom in range(row_top, rows):
            for col_left in range(cols):
                for col_right in range(col_left, cols):
                    submatrix = matrix[row_top:row_bottom + 1, col_left:col_right + 1]
                    if submatrix.size == n:
                        count += 1
    return count