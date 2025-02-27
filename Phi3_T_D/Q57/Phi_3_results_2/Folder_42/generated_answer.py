import numpy as np
from itertools import product

def submatrix_with_particular_sum(matrix):
    nrows, ncols = matrix.shape
    submatrices = []
    for rows in range(1, nrows + 1):
        for cols in range(1, ncols + 1):
            for i in range(nrows - rows + 1):
                for j in range(ncols - cols + 1):
                    submatrix = matrix[i:i + rows, j:j + cols]
                    if np.sum(submatrix) == 862:
                        submatrices.append(submatrix)
    return submatrices