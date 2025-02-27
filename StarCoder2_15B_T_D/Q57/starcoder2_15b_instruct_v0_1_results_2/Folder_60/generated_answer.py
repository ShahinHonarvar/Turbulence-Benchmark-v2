import numpy as np

def submatrix_with_particular_sum(matrix):
    m, n = matrix.shape
    submatrices = []
    for i in range(m - 2):
        for j in range(n - 2):
            submatrix = matrix[i:i + 3, j:j + 3]
            if np.sum(submatrix) == 94:
                submatrices.append(submatrix)
    return submatrices