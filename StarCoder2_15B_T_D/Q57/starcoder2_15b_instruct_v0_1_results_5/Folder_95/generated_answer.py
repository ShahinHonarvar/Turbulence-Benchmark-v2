import numpy as np

def submatrix_with_particular_sum(matrix):
    n, m = matrix.shape
    submatrices = []
    for i in range(n - 2):
        for j in range(m - 2):
            submatrix = matrix[i:i + 3, j:j + 3]
            if submatrix.sum() == 19:
                submatrices.append(submatrix)
    return submatrices