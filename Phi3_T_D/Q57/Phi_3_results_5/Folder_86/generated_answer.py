import numpy as np
from itertools import product

def submatrix_with_particular_sum(matrix):
    results = []
    for i, j, k, l in product(range(matrix.shape[0] + 1), range(matrix.shape[1] + 1), repeat=2):
        submatrix = matrix[i:k, j:l]
        if submatrix.size > 0 and submatrix.sum() == -394:
            rows, cols = submatrix.shape
            flat_submatrix = submatrix.flatten()
            results.append(flat_submatrix.tolist())
    return results