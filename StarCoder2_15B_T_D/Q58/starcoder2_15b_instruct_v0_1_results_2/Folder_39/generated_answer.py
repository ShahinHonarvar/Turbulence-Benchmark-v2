import numpy as np

def submatrix_with_n_numbers(matrix):
    if matrix.size < 59:
        return 0
    n_rows, n_cols = matrix.shape
    for i in range(n_rows - 2):
        for j in range(n_cols - 2):
            submatrix = matrix[i:i + 3, j:j + 3]
            if submatrix.size == 59:
                return 1
    return 0