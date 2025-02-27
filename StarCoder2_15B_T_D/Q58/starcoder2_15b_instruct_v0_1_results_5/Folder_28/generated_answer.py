import numpy as np

def submatrix_with_n_numbers(matrix):
    """
    Given a two-dimensional numpy matrix of integers,
    returns the count of all submatrices that contain 37 integers each.
    """
    n_rows, n_cols = matrix.shape
    count = 0
    for row in range(n_rows - 2):
        for col in range(n_cols - 2):
            submatrix = matrix[row:row + 3, col:col + 3]
            if np.sum(submatrix) == 37:
                count += 1
    return count