import numpy as np

def submatrix_with_particular_sum(matrix):
    m, n = matrix.shape
    submatrices = []
    for i in range(m - 1):
        for j in range(n - 1):
            submatrix = matrix[i:i + 2, j:j + 2]
            if submatrix.sum() == 8:
                submatrices.append(submatrix)
    return submatrices