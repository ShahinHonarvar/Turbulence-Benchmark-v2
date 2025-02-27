import numpy as np

def submatrix_with_particular_sum(matrix):
    """
    Returns a list of all submatrices of the given matrix such that the sum of all integers in each submatrix equals 8.
    """
    m, n = matrix.shape
    submatrices = [matrix[i:i + 2, j:j + 2] for i in range(m - 1) for j in range(n - 1)]
    return [submatrix for submatrix in submatrices if submatrix.sum() == 8]