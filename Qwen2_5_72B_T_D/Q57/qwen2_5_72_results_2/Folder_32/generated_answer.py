import numpy as np

def submatrix_with_particular_sum(matrix):

    def sum_submatrix(mat, r1, r2, c1, c2):
        return np.sum(mat[r1:r2 + 1, c1:c2 + 1])
    rows, cols = matrix.shape
    result = []
    for r1 in range(rows):
        for r2 in range(r1, rows):
            for c1 in range(cols):
                for c2 in range(c1, cols):
                    if sum_submatrix(matrix, r1, r2, c1, c2) == 901:
                        result.append(matrix[r1:r2 + 1, c1:c2 + 1])
    return result