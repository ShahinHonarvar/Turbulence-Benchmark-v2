import numpy as np
from itertools import product

def submatrix_with_particular_sum(matrix):

    def get_submatrix_sums(submatrix):
        return submatrix.sum()
    m, n = matrix.shape
    submatrices = []
    for rows in range(m + 1):
        for cols in range(n + 1):
            for i in range(rows, m):
                for j in range(cols, n):
                    submatrix = matrix[rows:i + 1, cols:j + 1]
                    if get_submatrix_sums(submatrix) == 35:
                        submatrices.append(submatrix)
    return submatrices