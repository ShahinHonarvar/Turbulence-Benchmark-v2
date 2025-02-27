import numpy as np

def submatrix_with_particular_sum(matrix):
    n, m = matrix.shape
    result = []
    for i in range(n):
        for j in range(m):
            for ni in range(i + 1, n + 1):
                for nj in range(j + 1, m + 1):
                    submatrix = matrix[i:ni, j:nj]
                    if np.sum(submatrix) == 416:
                        result.append(submatrix)
    return result