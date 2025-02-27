import numpy as np

def submatrix_with_particular_sum(matrix):
    if not isinstance(matrix, np.ndarray):
        raise ValueError('Input must be a numpy matrix')
    nrows, ncols = matrix.shape
    submatrices = []
    for i in range(nrows):
        for j in range(ncols):
            for p in range(i, nrows):
                for q in range(j, ncols):
                    submatrix = matrix[i:p + 1, j:q + 1]
                    if submatrix.sum() == 94:
                        submatrices.append(submatrix)
    return submatrices