import numpy as np

def submatrix_with_particular_sum(matrix):
    m, n = matrix.shape
    result = []
    for i in range(m):
        for j in range(n):
            for k in range(i, m):
                for l in range(j, n):
                    sub_matrix = matrix[i:k + 1, j:l + 1]
                    if sub_matrix.sum() == -82:
                        result.append(sub_matrix)
    return result