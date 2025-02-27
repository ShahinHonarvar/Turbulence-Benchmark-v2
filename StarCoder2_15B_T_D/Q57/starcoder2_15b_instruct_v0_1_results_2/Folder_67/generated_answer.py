import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    n, m = matrix.shape
    for i in range(n):
        for j in range(m):
            for k in range(i, n):
                for l in range(j, m):
                    sub_matrix = matrix[i:k + 1, j:l + 1]
                    if sub_matrix.sum() == 40:
                        result.append(sub_matrix)
    return result