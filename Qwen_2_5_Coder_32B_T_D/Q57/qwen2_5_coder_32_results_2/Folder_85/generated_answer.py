import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    m, n = matrix.shape
    for i in range(m):
        for j in range(n):
            for rows in range(i + 1, m + 1):
                for cols in range(j + 1, n + 1):
                    submatrix = matrix[i:rows, j:cols]
                    if np.sum(submatrix) == -87:
                        result.append(submatrix)
    return result