import numpy as np

def submatrix_with_n_numbers(matrix):
    if matrix.size < 185:
        return 0
    n_rows, n_cols = matrix.shape
    for i in range(n_rows - 3):
        for j in range(n_cols - 3):
            submatrix = matrix[i:i + 4, j:j + 4]
            if submatrix.size == 185:
                return 1
    return 0