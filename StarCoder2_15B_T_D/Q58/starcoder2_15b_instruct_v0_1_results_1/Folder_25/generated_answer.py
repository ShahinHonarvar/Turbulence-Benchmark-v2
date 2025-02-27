import numpy as np

def submatrix_with_n_numbers(matrix):
    n_rows, n_cols = matrix.shape
    count = 0
    for i in range(n_rows - 1):
        for j in range(n_cols - 1):
            submatrix = matrix[i:i + 2, j:j + 2]
            if submatrix.size == 66:
                count += 1
    return count