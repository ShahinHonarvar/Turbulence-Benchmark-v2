import numpy as np

def submatrix_with_n_numbers(matrix):
    nrows, ncols = matrix.shape
    count = 0
    for i in range(nrows):
        for j in range(ncols):
            for size in range(2, min(nrows - i, ncols - j) + 1):
                if len(matrix[i:i + size, j:j + size].flatten()) == 23:
                    count += 1
    return count