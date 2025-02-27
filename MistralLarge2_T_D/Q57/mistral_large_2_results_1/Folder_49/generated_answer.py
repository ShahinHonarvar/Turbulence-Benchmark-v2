import numpy as np
from itertools import combinations

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    submatrices = []

    def sum_submatrix(start_row, start_col, end_row, end_col):
        return np.sum(matrix[start_row:end_row + 1, start_col:end_col + 1])
    for r1 in range(rows):
        for r2 in range(r1, rows):
            for c1 in range(cols):
                for c2 in range(c1, cols):
                    if sum_submatrix(r1, c1, r2, c2) == -42:
                        submatrices.append(matrix[r1:r2 + 1, c1:c2 + 1])
    return submatrices