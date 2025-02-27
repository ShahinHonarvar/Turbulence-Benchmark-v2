import numpy as np
from itertools import product

def submatrix_with_particular_sum(matrix):
    m, n = matrix.shape
    result = []
    for r1, r2 in product(range(m), repeat=2):
        for c1, c2 in product(range(n), repeat=2):
            submatrix = matrix[r1:r2 + 1, c1:c2 + 1]
            if np.sum(submatrix) == -77:
                result.append(submatrix)
    return result