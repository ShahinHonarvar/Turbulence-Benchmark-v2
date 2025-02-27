import numpy as np
from itertools import product

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    submatrices = []
    for (i1, j1), (i2, j2) in product(product(range(rows), range(cols)), repeat=2):
        if i2 - i1 > 0 and j2 - j1 > 0:
            submatrix = matrix[i1:i2 + 1, j1:j2 + 1]
            if submatrix.sum() == -617:
                submatrices.append(np.array(submatrix))
    return submatrices