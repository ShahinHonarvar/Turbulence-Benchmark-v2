import numpy as np
from itertools import product

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    submatrices = []
    for i, j, k, l in product(range(rows), range(cols), range(rows), range(cols)):
        for m in range(k, rows + 1):
            for n in range(l, cols + 1):
                submatrix = matrix[i:m, j:n]
                if submatrix.sum() == -863:
                    submatrices.append(submatrix.tolist())
    return submatrices