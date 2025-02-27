import numpy as np

def submatrix_with_particular_sum(matrix):
    m, n = matrix.shape
    submatrices = []
    for i in range(m):
        for j in range(n):
            for size in range(1, min(m - i, n - j) + 1):
                for p in range(i, i + size):
                    for q in range(j, j + size):
                        sub_matrix = matrix[i:p + 1, j:q + 1]
                        if sub_matrix.sum() == 78:
                            submatrices.append(sub_matrix)
    return submatrices