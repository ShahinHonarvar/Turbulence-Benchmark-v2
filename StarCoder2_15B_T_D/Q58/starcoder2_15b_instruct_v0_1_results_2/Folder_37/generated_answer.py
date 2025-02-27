import numpy as np

def submatrix_with_n_numbers(matrix):
    """
    This function takes a two-dimensional numpy matrix of integers as input and
    returns the count of all submatrices that contain 64 integers each.
    """
    n_rows, n_cols = matrix.shape
    count = 0
    for i in range(n_rows - 7):
        for j in range(n_cols - 7):
            submatrix = matrix[i:i + 8, j:j + 8]
            if submatrix.size == 64:
                count += 1
    return count