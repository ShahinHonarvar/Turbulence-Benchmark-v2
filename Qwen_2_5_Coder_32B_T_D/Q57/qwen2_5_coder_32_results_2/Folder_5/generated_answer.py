import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    m, n = matrix.shape
    for i in range(m):
        for j in range(n):
            for ii in range(i, m):
                for jj in range(j, n):
                    if np.sum(matrix[i:ii + 1, j:jj + 1]) == -43:
                        result.append(matrix[i:ii + 1, j:jj + 1])
    return result