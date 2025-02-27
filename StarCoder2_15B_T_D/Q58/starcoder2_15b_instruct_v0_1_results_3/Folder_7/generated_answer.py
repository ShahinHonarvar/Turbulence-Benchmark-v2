import numpy as np

def submatrix_with_n_numbers(matrix):
    """
    Function to count submatrices of the given matrix that contain 121 integers each.
    """
    num_submatrices = 0
    n = 121
    for i in range(len(matrix) - n + 1):
        for j in range(len(matrix[0]) - n + 1):
            submatrix = matrix[i:i + n, j:j + n]
            num_submatrices += 1
    return num_submatrices