import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 94
    submatrices = []
    for i in range(len(matrix) - n + 1):
        for j in range(len(matrix[0]) - n + 1):
            submatrix = matrix[i:i + n, j:j + n]
            if submatrix.size == n:
                submatrices.append(submatrix)
    return len(submatrices)