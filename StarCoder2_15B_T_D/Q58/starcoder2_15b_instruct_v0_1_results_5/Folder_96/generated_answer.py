import numpy as np

def submatrix_with_n_numbers(matrix):
    n_rows, n_cols = matrix.shape
    count = 0
    for i in range(n_rows - 19):
        for j in range(n_cols - 19):
            submatrix = matrix[i:i + 20, j:j + 20]
            if submatrix.size == 20:
                count += 1
    return count