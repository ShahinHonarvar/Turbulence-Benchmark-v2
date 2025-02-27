import numpy as np
from itertools import product

def submatrix_with_particular_sum(matrix):

    def submatrix_sum(m, r1, c1, r2, c2):
        return np.sum(m[r1:r2, c1:c2])
    results = []
    rows, cols = matrix.shape
    for size in range(1, rows + 1):
        for i, j in product(range(rows - size + 1), range(cols - size + 1)):
            submatrix = matrix[i:i + size, j:j + size]
            if submatrix_sum(submatrix, 0, 0, size, size) == -90:
                results.append(submatrix)
    return results