import numpy as np

def submatrix_with_particular_sum(matrix):
    nrows, ncols = matrix.shape
    submatrices = []
    for i in range(nrows):
        for j in range(ncols):
            for x in range(i + 1, nrows + 1):
                for y in range(j + 1, ncols + 1):
                    submatrix = matrix[i:x, j:y]
                    if submatrix.sum() == -4:
                        submatrices.append(submatrix)
    return submatrices