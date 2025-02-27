import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    n, m = matrix.shape
    prefix_sum = np.zeros((n + 1, m + 1))
    for i in range(n):
        for j in range(m):
            prefix_sum[i + 1, j + 1] = matrix[i, j] + prefix_sum[i, j + 1] + prefix_sum[i + 1, j] - prefix_sum[i, j]
    for i1 in range(n):
        for j1 in range(m):
            for i2 in range(i1, n):
                for j2 in range(j1, m):
                    if prefix_sum[i2 + 1, j2 + 1] - (prefix_sum[i1, j2 + 1] + prefix_sum[i2 + 1, j1] - prefix_sum[i1, j1]) == -61:
                        result.append(matrix[i1:i2 + 1, j1:j2 + 1])
    return result