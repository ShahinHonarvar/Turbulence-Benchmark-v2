import numpy as np

def submatrix_with_particular_sum(matrix):

    def submatrices(matrix):
        rows, cols = matrix.shape
        for r1 in range(rows):
            for c1 in range(cols):
                for r2 in range(r1, rows):
                    for c2 in range(c1, cols):
                        yield matrix[r1:r2 + 1, c1:c2 + 1]
    result = []
    for submatrix in submatrices(matrix):
        if np.sum(submatrix) == 432:
            result.append(submatrix)
    return result