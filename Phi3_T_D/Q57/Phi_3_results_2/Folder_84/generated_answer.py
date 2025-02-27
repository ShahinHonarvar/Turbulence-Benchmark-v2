import numpy as np

def submatrix_with_particular_sum(matrix):
    nrows, ncols = matrix.shape
    candidates = []
    for i in range(nrows):
        for j in range(ncols):
            for k in range(i, nrows):
                for l in range(j, ncols):
                    submatrix = matrix[i:k + 1, j:l + 1]
                    if np.sum(submatrix) == -308:
                        candidates.append(submatrix)
    return candidates