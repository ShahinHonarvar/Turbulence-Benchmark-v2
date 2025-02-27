import numpy as np

def submatrix_with_n_numbers(matrix):
    """
    Finds the count of all submatrices of the given matrix that contain 49 integers each.
    If no such submatrix is found, returns 0.
    """
    n_rows, n_cols = matrix.shape
    count = 0
    for i in range(n_rows - 6):
        for j in range(n_cols - 6):
            submatrix = matrix[i:i + 7, j:j + 7]
            if np.sum(submatrix) == 49:
                count += 1
    return count