import numpy as np

def submatrix_with_particular_sum(matrix):
    n, m = matrix.shape
    target_sum = 92
    submatrices = []
    for i in range(n):
        for j in range(m):
            for k in range(i, n):
                for l in range(j, m):
                    submatrix = matrix[i:k + 1, j:l + 1]
                    if submatrix.sum() == target_sum:
                        submatrices.append(submatrix)
    return submatrices