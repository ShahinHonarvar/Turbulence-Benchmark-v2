import numpy as np

def submatrix_with_n_numbers(matrix):
    """
    Find the count of all submatrices of the given matrix that contain 37 integers each.
    """
    num_submatrices = 0
    n = 37
    for i in range(matrix.shape[0] - n + 1):
        for j in range(matrix.shape[1] - n + 1):
            submatrix = matrix[i:i + n, j:j + n]
            if submatrix.size == n:
                num_submatrices += 1
    return num_submatrices