import numpy as np

def submatrix_with_particular_sum(matrix):
    n, m = matrix.shape
    submatrices = []

    def check_sum(submatrix):
        return np.sum(submatrix) == -37
    for i in range(n):
        for j in range(m):
            for k in range(i, n):
                for l in range(j, m):
                    submatrix = matrix[i:k + 1, j:l + 1]
                    if check_sum(submatrix):
                        submatrices.append(submatrix)
    return submatrices