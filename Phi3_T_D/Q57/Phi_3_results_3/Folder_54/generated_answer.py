import numpy as np
from itertools import product

def submatrix_with_particular_sum(matrix):
    nrows, ncols = matrix.shape
    result = []
    for rows in range(1, nrows + 1):
        for cols in range(1, ncols + 1):
            for row_start in range(nrows - rows + 1):
                for col_start in range(ncols - cols + 1):
                    submatrix = matrix[row_start:row_start + rows, col_start:col_start + cols]
                    if submatrix.sum() == -59:
                        result.append(submatrix)
    return result