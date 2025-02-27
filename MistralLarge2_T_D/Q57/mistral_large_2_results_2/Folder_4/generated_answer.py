import numpy as np
from itertools import combinations

def submatrix_with_particular_sum(matrix):
    result = []
    rows, cols = matrix.shape

    def submatrices(start_row, end_row, start_col, end_col):
        return matrix[start_row:end_row + 1, start_col:end_col + 1]

    def check_submatrices():
        for r1, r2 in combinations(range(rows), 2):
            for c1, c2 in combinations(range(cols), 2):
                submatrix = submatrices(r1, r2, c1, c2)
                if np.sum(submatrix) == 87:
                    result.append(submatrix)
    if rows > 1 and cols > 1:
        check_submatrices()
    return result