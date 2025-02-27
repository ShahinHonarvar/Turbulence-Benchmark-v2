import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    nrows, ncols = matrix.shape
    for size in range(1, nrows + 1):
        for row in range(nrows - size + 1):
            for col in range(ncols - size + 1):
                submatrix = matrix[row:row + size, col:col + size]
                if submatrix.size == 159:
                    count += 1
    return count