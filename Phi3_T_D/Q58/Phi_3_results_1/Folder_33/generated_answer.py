import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    nrows, ncols = matrix.shape
    given_n = 118
    for i in range(nrows):
        for j in range(ncols):
            if i + given_n - 1 < nrows and j + given_n - 1 < ncols:
                submatrix = matrix[i:i + given_n, j:j + given_n]
                if np.all(submatrix == given_n):
                    count += 1
    return count