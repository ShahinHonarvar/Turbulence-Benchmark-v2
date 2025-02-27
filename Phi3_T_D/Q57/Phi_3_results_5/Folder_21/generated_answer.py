import numpy as np
from itertools import product

def submatrix_with_particular_sum(matrix):
    targets = []
    rows, cols = matrix.shape
    target_sum = -936
    for r1, r2 in product(range(rows), repeat=2):
        for c1, c2 in product(range(cols), repeat=2):
            submatrix = matrix[r1:r2 + 1, c1:c2 + 1]
            if submatrix.sum() == target_sum:
                targets.append(submatrix)
    return targets