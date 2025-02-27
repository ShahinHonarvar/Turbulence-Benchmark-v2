import numpy as np

def submatrix_with_particular_sum(matrix):
    nrows, ncols = matrix.shape
    res = []
    for i in range(nrows):
        for j in range(ncols):
            for k in range(i + 1, nrows + 1):
                for l in range(j + 1, ncols + 1):
                    submat = matrix[i:k, j:l]
                    if submat.sum() == 59:
                        res.append(submat)
    return res