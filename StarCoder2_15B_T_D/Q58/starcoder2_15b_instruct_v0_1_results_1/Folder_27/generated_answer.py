import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 77
    num_submatrices = 0
    row, col = matrix.shape
    for i in range(row - n + 1):
        for j in range(col - n + 1):
            submatrix = matrix[i:i + n, j:j + n]
            if submatrix.size == n:
                num_submatrices += 1
    return num_submatrices