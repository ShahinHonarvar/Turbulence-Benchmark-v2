import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    submatrices = []

    def get_all_submatrices(r1, c1, rows, cols):
        for r2 in range(r1, rows):
            for c2 in range(c1, cols):
                submatrix = matrix[r1:r2 + 1, c1:c2 + 1]
                if np.sum(submatrix) == 411:
                    submatrices.append(submatrix)
    for i in range(rows):
        for j in range(cols):
            get_all_submatrices(i, j, rows, cols)
    return submatrices