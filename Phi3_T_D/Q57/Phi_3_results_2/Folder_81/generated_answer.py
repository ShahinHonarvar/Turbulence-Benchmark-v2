import numpy as np

def submatrix_with_particular_sum(matrix):
    n, m = matrix.shape
    result = []
    for i in range(n):
        for j in range(m):
            for k in range(i, n):
                for l in range(j, m):
                    submatrix = matrix[i:k + 1, j:l + 1]
                    if submatrix.sum() == -90:
                        result.append(submatrix)
    return result