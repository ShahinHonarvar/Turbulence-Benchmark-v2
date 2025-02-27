import numpy as np

def submatrix_with_n_numbers(matrix):
    size = matrix.size
    if size < 74:
        return 0
    count = 0
    rows, cols = matrix.shape
    for row_end in range(rows):
        for col_end in range(cols):
            for row_start in range(row_end + 1, rows + 1):
                for col_start in range(col_end + 1, cols + 1):
                    submatrix = matrix[row_start - 1:row_end, col_start - 1:col_end]
                    if submatrix.size >= 74:
                        count += 1
    return count