import numpy as np

def submatrix_with_n_numbers(matrix):
    nrows, ncols = matrix.shape
    count = 0
    for i in range(nrows):
        for j in range(ncols):
            for x in range(i, nrows):
                for y in range(j, ncols):
                    submatrix = matrix[i:x + 1, j:y + 1]
                    if np.count_nonzero(submatrix) == 97:
                        count += 1
    return count