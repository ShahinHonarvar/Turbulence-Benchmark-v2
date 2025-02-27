import numpy as np

def submatrix_with_particular_sum(matrix):
    """
    Finds all submatrices of the given matrix such that the sum of all integers in each submatrix equals 16.
    """
    submatrices = []
    for i in range(matrix.shape[0] - 1):
        for j in range(matrix.shape[1] - 1):
            submatrix = matrix[i:i + 2, j:j + 2]
            if submatrix.sum() == 16:
                submatrices.append(submatrix)
    return submatrices