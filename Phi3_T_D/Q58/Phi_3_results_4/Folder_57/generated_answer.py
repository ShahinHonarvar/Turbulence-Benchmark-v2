import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for row_top in range(rows):
        for col_left in range(cols):
            for row_bottom in range(row_top, rows):
                for col_right in range(col_left, cols):
                    submatrix = matrix[row_top:row_bottom + 1, col_left:col_right + 1]
                    if submatrix.size == 92:
                        count += 1
    return count