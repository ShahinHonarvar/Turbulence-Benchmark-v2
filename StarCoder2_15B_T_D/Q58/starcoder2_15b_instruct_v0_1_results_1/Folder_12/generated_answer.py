import numpy as np

def submatrix_with_n_numbers(matrix):
    """
    Returns the count of all submatrices of the given matrix
    that contain 46 integers each. If no such submatrix is found, 
    the function returns 0.
    """
    n_rows, n_cols = matrix.shape
    count = 0
    for i in range(n_rows - 1):
        for j in range(n_cols - 1):
            submatrix = matrix[i:i + 2, j:j + 2]
            if np.sum(submatrix) == 46:
                count += 1
    return count