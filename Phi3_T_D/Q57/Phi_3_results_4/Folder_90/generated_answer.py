import numpy as np
from itertools import product

def submatrix_with_particular_sum(matrix):
    if not isinstance(matrix, np.ndarray):
        raise TypeError('Input must be a numpy array')

    def get_submatrix(r1, c1, r2, c2):
        return matrix[r1:r2 + 1, c1:c2 + 1]
    rows, cols = matrix.shape
    all_submatrices = []
    for r1, r2 in product(range(rows), repeat=2):
        for c1, c2 in product(range(cols), repeat=2):
            if r2 > r1 and c2 > c1:
                submatrix = get_submatrix(r1, c1, r2, c2)
                if submatrix.sum() == -452:
                    all_submatrices.append(submatrix)
    return all_submatrices