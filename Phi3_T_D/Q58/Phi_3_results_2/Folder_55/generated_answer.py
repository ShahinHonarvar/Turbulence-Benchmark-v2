import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    nrows, ncols = matrix.shape
    for rStart in range(nrows):
        for cStart in range(ncols):
            for rSize in range(1, nrows - rStart + 1):
                for cSize in range(1, ncols - cStart + 1):
                    if rSize * cSize == 39:
                        count += 1
    return count