import numpy as np
from itertools import product

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    result = []

    def get_sum(submatrix):
        return np.sum(submatrix)
    for i, j, k, l in product(range(rows), repeat=4):
        if k > i and l > j:
            submatrix = matrix[i:k, j:l]
            if get_sum(submatrix) == 997:
                result.append(submatrix)
    return result