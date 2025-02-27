import numpy as np

def submatrix_with_particular_sum(matrix):
    nrows, ncols = matrix.shape
    valid_submatrices = []
    for i in range(nrows):
        for j in range(ncols):
            for size in range(1, min(nrows - i, ncols - j) + 1):
                submatrix = matrix[i:i + size, j:j + size]
                if np.sum(submatrix) == 901:
                    valid_submatrices.append(submatrix.tolist())
    return valid_submatrices