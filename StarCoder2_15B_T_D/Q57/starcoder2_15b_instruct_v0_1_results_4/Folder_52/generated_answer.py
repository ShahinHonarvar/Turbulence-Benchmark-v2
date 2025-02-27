import numpy as np

def submatrix_with_particular_sum(matrix):
    n, m = matrix.shape
    submatrices = []
    for row_start in range(n):
        for row_end in range(row_start + 1, n + 1):
            for col_start in range(m):
                for col_end in range(col_start + 1, m + 1):
                    submatrix = matrix[row_start:row_end, col_start:col_end]
                    if np.sum(submatrix) == 100:
                        submatrices.append(submatrix)
    return submatrices