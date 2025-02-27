import numpy as np

def submatrix_with_particular_sum(matrix):
    if not isinstance(matrix, np.ndarray):
        raise ValueError('Input must be a numpy array')
    nrows, ncols = matrix.shape
    submatrices = []
    for i in range(nrows):
        for j in range(ncols):
            for h in range(i, nrows):
                for w in range(j, ncols):
                    submatrix = matrix[i:h + 1, j:w + 1]
                    if submatrix.sum() == 88:
                        submatrices.append(submatrix)
    return submatrices