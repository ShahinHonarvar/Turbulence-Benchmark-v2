import numpy as np

def submatrix_with_particular_sum(matrix):

    def all_submatrices(matrix):
        rows, cols = matrix.shape
        submatrices = []
        for r1 in range(rows):
            for c1 in range(cols):
                for r2 in range(r1, rows):
                    for c2 in range(c1, cols):
                        submatrices.append(matrix[r1:r2 + 1, c1:c2 + 1])
        return submatrices
    submatrices = all_submatrices(matrix)
    result = [submatrix for submatrix in submatrices if np.sum(submatrix) == 245]
    return result