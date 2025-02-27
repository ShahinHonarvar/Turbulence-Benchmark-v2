import numpy as np

def submatrix_with_particular_sum(matrix):
    nrows, ncols = matrix.shape
    results = []
    for i in range(nrows):
        for j in range(ncols):
            for size in range(1, nrows - i + 1):
                for width in range(1, ncols - j + 1):
                    candidate = matrix[i:i + size, j:j + width]
                    if np.sum(candidate) == -128:
                        results.append(candidate)
    return results