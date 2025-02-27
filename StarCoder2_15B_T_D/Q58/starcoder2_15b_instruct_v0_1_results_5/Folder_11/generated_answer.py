import numpy as np

def submatrix_with_n_numbers(matrix):
    submatrix_count = 0
    n = 38
    rows, cols = matrix.shape
    for i in range(rows - 2):
        for j in range(cols - 2):
            submatrix = matrix[i:i + 3, j:j + 3]
            if np.sum(submatrix) == n:
                submatrix_count += 1
    return submatrix_count