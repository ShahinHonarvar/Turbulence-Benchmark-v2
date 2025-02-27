import numpy as np
from itertools import product

def submatrix_with_particular_sum(matrix):
    m, n = matrix.shape
    submatrices = []
    for size in range(1, min(m, n) + 1):
        for row_start in range(m - size + 1):
            for col_start in range(n - size + 1):
                submatrix = matrix[row_start:row_start + size, col_start:col_start + size]
                if submatrix.sum() == -81:
                    submatrices.append(submatrix)
    return submatrices