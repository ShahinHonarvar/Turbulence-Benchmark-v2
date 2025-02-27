import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    n, m = matrix.shape
    for i in range(n):
        for j in range(m):
            for di in range(i, n):
                for dj in range(j, m):
                    submatrix = matrix[i:di + 1, j:dj + 1]
                    if np.sum(submatrix) == -779:
                        result.append(submatrix)
    return result