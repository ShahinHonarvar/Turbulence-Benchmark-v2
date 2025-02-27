import numpy as np
from itertools import product

def submatrix_with_particular_sum(matrix):
    n_rows, n_cols = matrix.shape
    submatrices = []
    for r1, r2 in product(range(n_rows), repeat=2):
        for c1, c2 in product(range(n_cols), repeat=2):
            for i in range(r2 - r1 + 1):
                for j in range(c2 - c1 + 1):
                    submatrix = matrix[r1:r2 + i, c1:c2 + j]
                    if np.sum(submatrix) == 3:
                        submatrices.append(submatrix)
    return submatrices