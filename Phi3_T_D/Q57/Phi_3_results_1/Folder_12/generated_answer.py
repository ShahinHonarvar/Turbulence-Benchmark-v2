import numpy as np

def submatrix_with_particular_sum(matrix):
    n, m = matrix.shape
    result = []
    for i in range(n):
        for j in range(m):
            for k in range(i, n):
                for l in range(j, m):
                    submat = matrix[i:k + 1, j:l + 1]
                    if np.sum(submat) == -83:
                        result.append(submat)
    return result