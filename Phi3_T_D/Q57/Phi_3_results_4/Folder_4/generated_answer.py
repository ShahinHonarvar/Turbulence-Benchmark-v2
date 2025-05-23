import numpy as np

def submatrix_with_particular_sum(matrix):
    m, n = matrix.shape
    total_submatrices = []
    for i in range(m):
        for j in range(n):
            for k in range(i + 1, m + 1):
                for l in range(j + 1, n + 1):
                    submatrix = matrix[i:k, j:l]
                    if submatrix.sum() == 87:
                        total_submatrices.append(submatrix)
    return total_submatrices