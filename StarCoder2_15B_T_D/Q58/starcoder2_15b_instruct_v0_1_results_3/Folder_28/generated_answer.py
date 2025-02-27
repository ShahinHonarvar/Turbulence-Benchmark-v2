import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 37
    num_submatrices = 0
    for i in range(matrix.shape[0] - n + 1):
        for j in range(matrix.shape[1] - n + 1):
            submatrix = matrix[i:i + n, j:j + n]
            if np.sum(submatrix) == n:
                num_submatrices += 1
    return num_submatrices