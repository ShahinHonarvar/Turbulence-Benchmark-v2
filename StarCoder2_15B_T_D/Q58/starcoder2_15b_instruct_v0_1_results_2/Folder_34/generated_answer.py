import numpy as np

def submatrix_with_n_numbers(matrix):
    """
    Given a two-dimensional numpy matrix of integers, return the count of all submatrices
    that contain 83 integers each. If no such submatrix is found, return 0.
    """
    n_rows, n_cols = matrix.shape
    count = 0
    for i in range(n_rows - 2):
        for j in range(n_cols - 2):
            submatrix = matrix[i:i + 3, j:j + 3]
            if np.sum(submatrix) == 83:
                count += 1
    return count