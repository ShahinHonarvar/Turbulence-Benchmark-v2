import numpy as np

def submatrix_with_particular_sum(matrix):
    """
    Finds all submatrices of the given matrix such that the sum of all integers in each submatrix equals 15.
    """
    submatrices = []
    for i in range(matrix.shape[0] - 2):
        for j in range(matrix.shape[1] - 2):
            submatrix = matrix[i:i + 3, j:j + 3]
            if np.sum(submatrix) == 15:
                submatrices.append(submatrix)
    return submatrices