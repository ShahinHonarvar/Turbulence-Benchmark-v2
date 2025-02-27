import numpy as np

def submatrix_with_n_numbers(matrix):
    row_count, col_count = matrix.shape
    count = 0
    for row_start in range(row_count - 3):
        for col_start in range(col_count - 3):
            submatrix = matrix[row_start:row_start + 4, col_start:col_start + 4]
            if submatrix.size == 13:
                count += 1
    return count