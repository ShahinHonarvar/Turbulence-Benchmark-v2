import numpy as np

def submatrix_with_particular_sum(matrix):
    nrows, ncols = matrix.shape
    res = []
    for i in range(nrows):
        for j in range(ncols):
            for k in range(i, nrows):
                for l in range(j, ncols):
                    if np.sum(matrix[i:k + 1, j:l + 1]) == -336:
                        res.append(matrix[i:k + 1, j:l + 1])
    return res