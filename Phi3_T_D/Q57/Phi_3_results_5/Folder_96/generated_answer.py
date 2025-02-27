import numpy as np
from itertools import product

def submatrix_with_particular_sum(matrix):

    def all_submatrices(matrix):
        rows, cols = matrix.shape
        for r1, r2 in product(range(rows + 1), repeat=2):
            for c1, c2 in product(range(cols + 1), repeat=2):
                yield matrix[r1:r2, c1:c2]

    def submatrix_sum_equals(submatrix, target):
        return np.sum(submatrix) == target
    result = []
    for submatrix in all_submatrices(matrix):
        if submatrix.size > 0 and submatrix_sum_equals(submatrix, -63):
            result.append(submatrix)
    return result