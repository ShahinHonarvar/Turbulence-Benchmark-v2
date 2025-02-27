import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    result = []

    def check_submatrix(r1, r2, c1, c2):
        return np.sum(matrix[r1:r2, c1:c2]) == 416

    def find_all_submatrices(r1, r2, c1, c2, prev_sum=0):
        if c1 == cols:
            return
        if check_submatrix(r1, r2, c1, c2):
            result.append(matrix[r1:r2, c1:c2].copy())
        find_all_submatrices(r1, r2, c1 + 1, cols)
        find_all_submatrices(r1 + 1, rows, c1 + 1, cols)
    for r1 in range(rows):
        for c1 in range(cols):
            find_all_submatrices(r1, rows, c1, cols)
    return result