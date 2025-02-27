import numpy as np

def submatrix_with_particular_sum(matrix):

    def all_submatrices(matrix):
        submatrices = []
        rows, cols = matrix.shape
        for r1 in range(rows):
            for r2 in range(r1, rows):
                for c1 in range(cols):
                    for c2 in range(c1, cols):
                        submatrices.append(matrix[r1:r2 + 1, c1:c2 + 1])
        return submatrices
    n = matrix.shape[0]
    submatrices = all_submatrices(matrix)
    result = [submatrix for submatrix in submatrices if np.sum(submatrix) == -6]
    return result