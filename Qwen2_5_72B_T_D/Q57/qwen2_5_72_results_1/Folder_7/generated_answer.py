import numpy as np

def submatrix_with_particular_sum(matrix):

    def sum_submatrix(mat, r1, c1, r2, c2):
        total = 0
        for r in range(r1, r2 + 1):
            for c in range(c1, c2 + 1):
                total += mat[r][c]
        return total
    submatrices = []
    rows, cols = matrix.shape
    for r1 in range(rows):
        for r2 in range(r1, rows):
            for c1 in range(cols):
                for c2 in range(c1, cols):
                    if sum_submatrix(matrix, r1, c1, r2, c2) == -128:
                        submatrices.append(matrix[r1:r2 + 1, c1:c2 + 1])
    return submatrices