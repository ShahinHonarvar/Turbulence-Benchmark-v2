import numpy as np

def submatrix_with_particular_sum(matrix):
    N, M = matrix.shape
    submatrices = []
    for i in range(N):
        for j in range(M):
            for k in range(i, N):
                for l in range(j, M):
                    submatrix_sum = np.sum(matrix[i:k + 1, j:l + 1])
                    if submatrix_sum == 432:
                        submatrices.append(matrix[i:k + 1, j:l + 1])
    return submatrices