import numpy as np

def submatrix_with_particular_sum(matrix):
    nrows, ncols = matrix.shape
    submatrices = []
    for x1 in range(nrows):
        for y1 in range(ncols):
            for x2 in range(x1, nrows):
                for y2 in range(y1, ncols):
                    submatrix = matrix[x1:x2 + 1, y1:y2 + 1]
                    if np.sum(submatrix) == 1:
                        submatrices.append(submatrix)
    return submatrices