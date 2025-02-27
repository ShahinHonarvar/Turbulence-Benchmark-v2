import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    nrows, ncols = matrix.shape
    for i in range(nrows):
        for j in range(ncols):
            for size in range(1, min(nrows - i, ncols - j) + 1):
                if np.sum(matrix[i:i + size, j:j + size]) == 73:
                    count += 1
    return count