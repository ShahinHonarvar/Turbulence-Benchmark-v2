import numpy as np
from itertools import product

def submatrix_with_particular_sum(matrix):
    shape = matrix.shape
    size = min(shape)
    submatrices = []
    for l in range(1, size + 1):
        for i, j in product(range(shape[0] - l + 1), range(shape[1] - l + 1)):
            submatrix = matrix[i:i + l, j:j + l]
            if submatrix.sum() == 21:
                submatrices.append(submatrix)
    return submatrices