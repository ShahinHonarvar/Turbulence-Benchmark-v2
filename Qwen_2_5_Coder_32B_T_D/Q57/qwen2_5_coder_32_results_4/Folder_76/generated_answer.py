import numpy as np

def submatrix_with_particular_sum(matrix):
    n, m = matrix.shape
    result = []
    for i in range(n):
        for j in range(m):
            for e in range(i, n):
                for f in range(j, m):
                    if np.sum(matrix[i:e + 1, j:f + 1]) == -255:
                        result.append(matrix[i:e + 1, j:f + 1])
    return result