import numpy as np
from itertools import product

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    result = []
    for r1 in range(1, rows + 1):
        for r2 in range(r1, rows + 1):
            for c1 in range(1, cols + 1):
                for c2 in range(c1, cols + 1):
                    submatrix = matrix[r1 - 1:r2, c1 - 1:c2]
                    if np.sum(submatrix) == 19:
                        result.append(submatrix)
    return result