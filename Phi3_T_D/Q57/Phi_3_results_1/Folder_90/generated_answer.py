import numpy as np
from itertools import product

def submatrix_with_particular_sum(matrix):
    nrows, ncols = matrix.shape
    result = []
    for sub_rows in range(1, nrows + 1):
        for sub_cols in range(1, ncols + 1):
            for i in range(nrows - sub_rows + 1):
                for j in range(ncols - sub_cols + 1):
                    submat = matrix[i:i + sub_rows, j:j + sub_cols]
                    if np.sum(submat) == -452:
                        result.append(submat)
    return result