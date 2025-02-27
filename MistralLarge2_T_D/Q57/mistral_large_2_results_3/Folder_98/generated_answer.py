import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    submatrices = []

    def find_submatrices(r1, c1, r2, c2):
        if r2 < rows and c2 < cols:
            submatrix = matrix[r1:r2 + 1, c1:c2 + 1]
            if submatrix.sum() == 0:
                submatrices.append(submatrix)
            find_submatrices(r1, c1, r2, c2 + 1)
            find_submatrices(r1, c1, r2 + 1, c2)
    for r1 in range(rows):
        for c1 in range(cols):
            find_submatrices(r1, c1, r1, c1)
    return submatrices