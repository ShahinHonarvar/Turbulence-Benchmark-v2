import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 186
    row_count, col_count = matrix.shape
    submatrix_count = 0
    for i in range(row_count - n + 1):
        for j in range(col_count - n + 1):
            submatrix = matrix[i:i + n, j:j + n]
            if np.sum(submatrix) == n:
                submatrix_count += 1
    return submatrix_count