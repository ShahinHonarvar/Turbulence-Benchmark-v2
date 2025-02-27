import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    m, n = matrix.shape
    for i in range(m):
        for j in range(n):
            for k in range(i + 1, m + 1):
                for l in range(j + 1, n + 1):
                    if len(matrix[i:k, j:l]) == 179:
                        count += 1
    return count