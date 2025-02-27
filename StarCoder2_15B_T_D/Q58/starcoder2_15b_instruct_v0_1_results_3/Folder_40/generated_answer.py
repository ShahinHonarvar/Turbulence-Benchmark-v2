import numpy as np

def submatrix_with_n_numbers(matrix):
    """
    Find the count of all submatrices of the given matrix that contain 1 integer each.
    """
    num_submatrices = 0
    nrows, ncols = matrix.shape
    for i in range(nrows):
        for j in range(ncols):
            if matrix[i, j] == 1:
                num_submatrices += 1
    return num_submatrices