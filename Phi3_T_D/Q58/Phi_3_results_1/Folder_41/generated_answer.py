import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    nrows, ncols = matrix.shape
    n = 73
    for i in range(nrows):
        for j in range(ncols):
            for size in range(1, min(nrows - i, ncols - j) + 1):
                submatrix = matrix[i:i + size, j:j + size]
                if submatrix.size == n and np.all(submatrix == 0):
                    count += 1
    return count