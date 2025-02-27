import numpy as np

def submatrix_with_n_numbers(matrix):
    """
    Finds the count of all submatrices of the given matrix that contain 107 integers each.
    If no such submatrix is found, returns 0.
    """
    n_rows, n_cols = matrix.shape
    count = 0
    for i in range(n_rows - 106):
        for j in range(n_cols - 106):
            submatrix = matrix[i:i + 107, j:j + 107]
            if np.sum(submatrix) == 107:
                count += 1
    return count