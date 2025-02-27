import numpy as np

def submatrix_with_n_numbers(matrix):
    if not isinstance(matrix, np.ndarray) or len(matrix.shape) != 2:
        return 0
    nrows, ncols = matrix.shape
    count = 0
    for i in range(nrows):
        for j in range(ncols):
            if j + 4 < ncols:
                for k in range(i + 4, nrows):
                    if np.all(matrix[i:k + 1, j:j + 5]):
                        count += 1
    return count