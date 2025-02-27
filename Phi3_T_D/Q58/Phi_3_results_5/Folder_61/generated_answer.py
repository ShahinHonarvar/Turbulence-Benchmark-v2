import numpy as np

def submatrix_with_n_numbers(matrix):
    nrows, ncols = matrix.shape
    count = 0
    for rowStart in range(nrows):
        for colStart in range(ncols):
            for rowEnd in range(rowStart, nrows):
                for colEnd in range(colStart, ncols):
                    if (rowEnd - rowStart + 1) * (colEnd - colStart + 1) == 4:
                        count += 1
    return count