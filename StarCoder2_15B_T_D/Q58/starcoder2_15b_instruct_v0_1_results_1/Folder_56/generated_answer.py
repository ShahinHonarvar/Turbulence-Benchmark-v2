import numpy as np

def submatrix_with_n_numbers(matrix):
    n_rows, n_cols = matrix.shape
    count = 0
    for i in range(n_rows - 67):
        for j in range(n_cols - 67):
            submatrix = matrix[i:i + 68, j:j + 68]
            if submatrix.size == 68:
                count += 1
    return count