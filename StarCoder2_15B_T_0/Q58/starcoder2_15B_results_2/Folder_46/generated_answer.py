import numpy as np

def submatrix_with_n_numbers(matrix):
    n_rows, n_cols = matrix.shape
    count = 0
    for i in range(n_rows - 13):
        for j in range(n_cols - 13):
            submatrix = matrix[i:i + 12, j:j + 12]
            if submatrix.size == 144:
                count += 1
    return count