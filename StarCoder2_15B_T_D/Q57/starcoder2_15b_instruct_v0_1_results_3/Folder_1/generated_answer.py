import numpy as np

def submatrix_with_particular_sum(matrix):
    """
    Finds all submatrices of the given matrix such that the sum of all integers in each submatrix equals -25.
    """
    submatrices = []
    nrows, ncols = matrix.shape
    for row in range(nrows):
        for col in range(ncols):
            for sub_nrows in range(1, nrows - row + 1):
                for sub_ncols in range(1, ncols - col + 1):
                    sub_matrix = matrix[row:row + sub_nrows, col:col + sub_ncols]
                    if np.sum(sub_matrix) == -25:
                        submatrices.append(sub_matrix)
    return submatrices