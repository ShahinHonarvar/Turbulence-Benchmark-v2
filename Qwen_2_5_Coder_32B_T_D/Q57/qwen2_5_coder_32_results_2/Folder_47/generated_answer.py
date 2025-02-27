import numpy as np

def submatrix_with_particular_sum(matrix):
    n, m = matrix.shape
    result = []
    for i in range(n):
        for j in range(m):
            for ni in range(i, n):
                for nj in range(j, m):
                    submatrix = matrix[i:ni + 1, j:nj + 1]
                    if np.sum(submatrix) == 27:
                        result.append(submatrix)
    return result