import numpy as np

def submatrix_with_n_numbers(matrix):
    n_rows, n_cols = matrix.shape
    count = 0
    for i in range(n_rows - 6 + 1):
        for j in range(n_cols - 6 + 1):
            submatrix = matrix[i:i + 6, j:j + 6]
            if submatrix.size == 48:
                count += 1
    return count