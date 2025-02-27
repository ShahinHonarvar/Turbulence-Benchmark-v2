import numpy as np

def submatrix_with_particular_sum(matrix):
    target_sum = -86
    submatrices = []
    for r1 in range(matrix.shape[0]):
        for r2 in range(r1, matrix.shape[0]):
            for c1 in range(matrix.shape[1]):
                for c2 in range(c1, matrix.shape[1]):
                    sub = matrix[r1:r2 + 1, c1:c2 + 1]
                    if np.sum(sub) == target_sum:
                        submatrices.append(sub)
    return submatrices