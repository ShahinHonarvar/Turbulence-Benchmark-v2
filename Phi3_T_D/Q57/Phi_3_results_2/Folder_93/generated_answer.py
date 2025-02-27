import numpy as np
from itertools import product

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    result = []
    for r1, r2 in product(range(rows), repeat=2):
        for c1, c2 in product(range(cols), repeat=2):
            if r1 <= r2 and c1 <= c2:
                submatrix_sum = np.sum(matrix[r1:r2 + 1, c1:c2 + 1])
                if submatrix_sum == -65:
                    result.append(matrix[r1:r2 + 1, c1:c2 + 1])
    return result