import numpy as np

def submatrix_with_particular_sum(matrix):
    M, N = matrix.shape
    result = []

    def check_sum(submatrix):
        return np.sum(submatrix) == -157
    for i in range(M):
        for j in range(N):
            for s1 in range(i, M):
                for s2 in range(j, N):
                    submatrix = matrix[i:s1 + 1, j:s2 + 1]
                    if check_sum(submatrix):
                        result.append(submatrix)
    return result