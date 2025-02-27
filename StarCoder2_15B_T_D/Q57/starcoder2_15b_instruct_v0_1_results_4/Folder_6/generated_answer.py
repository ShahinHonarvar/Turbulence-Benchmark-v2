import numpy as np

def submatrix_with_particular_sum(matrix):
    m, n = matrix.shape
    sum_matrix = np.zeros((m + 1, n + 1), dtype=int)
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            sum_matrix[i, j] = sum_matrix[i - 1, j] + sum_matrix[i, j - 1] - sum_matrix[i - 1, j - 1] + matrix[i - 1, j - 1]
    submatrices = []
    for i in range(m):
        for j in range(n):
            for k in range(i + 1, m + 1):
                for l in range(j + 1, n + 1):
                    submatrix_sum = sum_matrix[k, l] - sum_matrix[i, l] - sum_matrix[k, j] + sum_matrix[i, j]
                    if submatrix_sum == 126:
                        submatrices.append(matrix[i:k, j:l])
    return submatrices