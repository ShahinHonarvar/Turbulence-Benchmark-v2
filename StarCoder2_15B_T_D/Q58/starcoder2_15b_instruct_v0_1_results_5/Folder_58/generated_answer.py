import numpy as np

def submatrix_with_n_numbers(matrix):
    row_count, column_count = matrix.shape
    n = 185
    submatrix_count = 0
    for row_start in range(row_count - n + 1):
        for column_start in range(column_count - n + 1):
            submatrix = matrix[row_start:row_start + n, column_start:column_start + n]
            if submatrix.size == n:
                submatrix_count += 1
    return submatrix_count