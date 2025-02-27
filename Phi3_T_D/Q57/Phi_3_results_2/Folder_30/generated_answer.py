import numpy as np

def get_all_submatrices(matrix):
    nrows, ncols = matrix.shape
    submatrices = []
    for top in range(nrows):
        for left in range(ncols):
            for bottom in range(top + 1, nrows + 1):
                for right in range(left + 1, ncols + 1):
                    submatrix = matrix[top:bottom, left:right]
                    if np.sum(submatrix) == 21:
                        submatrices.append(submatrix)
    return submatrices

def submatrix_with_particular_sum(matrix):
    return get_all_submatrices(matrix)