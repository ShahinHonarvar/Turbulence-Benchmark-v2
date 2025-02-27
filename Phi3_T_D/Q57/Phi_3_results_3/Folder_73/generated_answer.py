import numpy as np
from itertools import product

def submatrix_with_particular_sum(matrix):
    n, m = matrix.shape
    target_sum = 93
    result = []
    for i, j in product(range(n), repeat=2):
        for k, l in product(range(i, n), repeat=2):
            for p, q in product(range(j, m), repeat=2):
                submatrix = matrix[i:k + 1, j:q + 1]
                if submatrix.sum() == target_sum:
                    result.append(submatrix)
    return result