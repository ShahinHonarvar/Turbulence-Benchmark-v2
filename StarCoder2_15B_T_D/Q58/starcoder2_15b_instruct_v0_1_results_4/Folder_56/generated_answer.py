import numpy as np

def submatrix_with_n_numbers(matrix):
    num_submatrices = 0
    n = 68
    m, n = matrix.shape
    for i in range(m - 2):
        for j in range(n - 2):
            submatrix = matrix[i:i + 3, j:j + 3]
            if submatrix.size == n:
                num_submatrices += 1
    return num_submatrices