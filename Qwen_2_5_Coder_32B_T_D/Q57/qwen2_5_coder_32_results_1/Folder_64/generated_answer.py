import numpy as np

def submatrix_with_particular_sum(matrix):
    m, n = matrix.shape
    result = []
    for i in range(m):
        for j in range(n):
            for k in range(i, m):
                for l in range(j, n):
                    if matrix[i:k + 1, j:l + 1].sum() == -4:
                        result.append(matrix[i:k + 1, j:l + 1])
    return result