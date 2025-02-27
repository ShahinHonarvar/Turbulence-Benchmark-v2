import numpy as np
from itertools import product

def submatrix_with_particular_sum(matrix):
    m, n = matrix.shape
    submatrices = []
    for x1, y1 in product(range(m), repeat=2):
        for x2, y2 in product(range(x1, m), repeat=2):
            for y3, x3 in product(range(y1, n), repeat=2):
                submatrix = matrix[x1:x2 + 1, y1:y3 + 1]
                if np.sum(submatrix) == 35:
                    submatrices.append(submatrix)
    return submatrices