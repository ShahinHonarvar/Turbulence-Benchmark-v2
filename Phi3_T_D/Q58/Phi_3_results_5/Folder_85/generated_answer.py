import numpy as np

def submatrix_with_n_numbers(matrix):
    nrows, ncols = matrix.shape
    count = 0
    for i in range(nrows):
        for j in range(ncols):
            for k in range(i, nrows):
                for l in range(j, ncols):
                    if (k - i + 1) * (l - j + 1) == 13:
                        submatrix = matrix[i:k + 1, j:l + 1]
                        if np.prod(submatrix.shape) == 13:
                            count += 1
    return count