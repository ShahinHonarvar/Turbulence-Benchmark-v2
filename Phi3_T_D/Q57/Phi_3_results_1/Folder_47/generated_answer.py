import numpy as np
from itertools import product

def submatrix_with_particular_sum(matrix):
    if not isinstance(matrix, np.ndarray):
        raise ValueError('Input must be a numpy matrix')
    sum_value = 27
    submatrices = []
    nrows, ncols = matrix.shape
    for i, j, k, l in product(range(nrows + 1), range(ncols + 1), repeat=2):
        submatrix = matrix[i:k, j:l]
        if submatrix.size > 0 and submatrix.sum() == sum_value:
            submatrices.append(submatrix)
    return submatrices