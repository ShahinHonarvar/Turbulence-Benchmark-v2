import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for row_begin in range(rows):
        for row_end in range(row_begin, rows):
            for col_begin in range(cols):
                for col_end in range(col_begin, cols):
                    submatrix = matrix[row_begin:row_end + 1, col_begin:col_end + 1]
                    size = submatrix.size
                    if size == 191:
                        count += 1
    return count