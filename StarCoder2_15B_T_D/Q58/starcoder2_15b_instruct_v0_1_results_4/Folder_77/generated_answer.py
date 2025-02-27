import numpy as np

def submatrix_with_n_numbers(matrix):
    m, n = matrix.shape
    for i in range(m):
        for j in range(n):
            for k in range(i, m):
                for l in range(j, n):
                    submatrix = matrix[i:k + 1, j:l + 1]
                    if submatrix.size == 179:
                        return 1
    return 0