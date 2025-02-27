import numpy as np
from itertools import combinations

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    submatrices = []

    def get_submatrices(start_row, end_row, start_col, end_col):
        return matrix[start_row:end_row + 1, start_col:end_col + 1]
    for r1, r2 in combinations(range(rows), 2):
        for c1, c2 in combinations(range(cols), 2):
            submatrix = get_submatrices(r1, r2, c1, c2)
            if np.sum(submatrix) == 1:
                submatrices.append(submatrix)
    return submatrices if submatrices else []