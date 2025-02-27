import numpy as np
import itertools

def submatrix_with_particular_sum(matrix):
    nrows, ncols = matrix.shape
    result = []
    for sz in range(1, nrows + 1):
        for i in range(nrows - sz + 1):
            for j in range(ncols - sz + 1):
                submat = matrix[i:i + sz, j:j + sz]
                if np.sum(submat) == 432:
                    result.append(submat)
    return result