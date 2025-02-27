import numpy as np

def submatrix_with_n_numbers(matrix, n=59):
    count = 0
    rows, cols = matrix.shape
    for row_start in range(rows):
        for row_end in range(row_start, rows):
            for col_start in range(cols):
                for col_end in range(col_start, cols):
                    submatrix = matrix[row_start:row_end + 1, col_start:col_end + 1]
                    if submatrix.size == n:
                        count += 1
    return count