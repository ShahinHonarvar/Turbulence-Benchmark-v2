import numpy as np
from itertools import product

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    submatrices = []
    for r1, r2 in product(range(rows), repeat=2):
        for c1, c2 in product(range(cols), repeat=2):
            for size in range(1, min(r2 - r1 + 1, c2 - c1 + 1) + 1):
                submatrix_sum = np.sum(matrix[r1:r1 + size, c1:c1 + size])
                if submatrix_sum == -936:
                    submatrices.append(matrix[r1:r1 + size, c1:c1 + size])
    return submatrices