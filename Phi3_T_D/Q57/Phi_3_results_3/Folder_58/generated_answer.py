import numpy as np
from itertools import product

def submatrix_with_particular_sum(matrix):
    height, width = matrix.shape
    submatrices = []
    for r1, r2 in product(range(height), repeat=2):
        for c1, c2 in product(range(width), repeat=2):
            if r2 > r1 and c2 > c1:
                sub = matrix[r1:r2, c1:c2]
                if sub.sum() == -137:
                    submatrices.append(sub)
    return submatrices