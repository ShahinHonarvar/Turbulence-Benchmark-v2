import numpy as np
from itertools import combinations

def submatrix_with_particular_sum(matrix):

    def get_submatrices(matrix):
        submatrices = []
        rows, cols = matrix.shape
        for r1, r2 in combinations(range(rows + 1), 2):
            for c1, c2 in combinations(range(cols + 1), 2):
                submatrix = matrix[r1:r2, c1:c2]
                submatrices.append(submatrix)
        return submatrices
    submatrices = get_submatrices(matrix)
    result = [submatrix for submatrix in submatrices if np.sum(submatrix) == 1]
    return result