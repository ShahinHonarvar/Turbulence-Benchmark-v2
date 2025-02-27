import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    submatrices = []
    for r1 in range(rows):
        for c1 in range(cols):
            for r2 in range(r1 + 1, rows + 1):
                for c2 in range(c1 + 1, cols + 1):
                    submatrix = matrix[r1:r2, c1:c2]
                    if np.sum(submatrix) == -6:
                        submatrices.append(submatrix)
    return submatrices