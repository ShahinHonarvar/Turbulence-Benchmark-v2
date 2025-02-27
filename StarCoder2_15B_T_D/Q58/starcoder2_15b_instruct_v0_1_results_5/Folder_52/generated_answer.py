import numpy as np

def submatrix_with_n_numbers(matrix):
    num_rows, num_cols = matrix.shape
    n = 147
    for i in range(num_rows - n + 1):
        for j in range(num_cols - n + 1):
            submatrix = matrix[i:i + n, j:j + n]
            if submatrix.size == n:
                return 1
    return 0