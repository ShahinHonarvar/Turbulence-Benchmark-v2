import numpy as np

def submatrix_with_n_numbers(matrix):
    """
    Returns the count of all submatrices of the given matrix that contain 95 integers each.
    If no such submatrix is found, returns 0.
    """
    n, m = matrix.shape
    count = 0
    for i in range(n - 2):
        for j in range(m - 2):
            submatrix = matrix[i:i + 3, j:j + 3]
            if np.sum(submatrix) == 95:
                count += 1
    return count