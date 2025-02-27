import numpy as np
from itertools import product

def submatrix_with_particular_sum(matrix):

    def is_valid_submatrix(submatrix):
        return np.sum(submatrix) == 862
    results = []
    nrows, ncols = matrix.shape
    for size in range(1, nrows + 1):
        for row_slice in range(nrows - size + 1):
            for col_slice in range(ncols - size + 1):
                submatrix = matrix[row_slice:row_slice + size, col_slice:col_slice + size]
                if is_valid_submatrix(submatrix):
                    results.append(submatrix.tolist())
    return results