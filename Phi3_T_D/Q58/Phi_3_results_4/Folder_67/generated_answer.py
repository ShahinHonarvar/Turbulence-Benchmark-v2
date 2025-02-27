import numpy as np

def submatrix_with_n_numbers(matrix):
    if not isinstance(matrix, np.ndarray):
        raise ValueError('Input must be a numpy matrix')
    nrows, ncols = matrix.shape
    count = 0
    for i in range(nrows):
        for j in range(ncols):
            for k in range(i, nrows):
                for l in range(j, ncols):
                    submatrix = matrix[i:k + 1, j:l + 1]
                    if np.unique(submatrix).size == 43:
                        count += 1
    return count