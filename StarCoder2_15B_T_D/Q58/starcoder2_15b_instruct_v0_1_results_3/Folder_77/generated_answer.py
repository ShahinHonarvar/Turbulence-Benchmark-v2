import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 179
    row_count, col_count = matrix.shape
    for i in range(row_count - n + 1):
        for j in range(col_count - n + 1):
            submatrix = matrix[i:i + n, j:j + n]
            if submatrix.size == n:
                return 1
    return 0