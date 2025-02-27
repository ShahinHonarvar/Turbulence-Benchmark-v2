import numpy as np

def submatrix_with_n_numbers(matrix):
    """
    Finds the count of all submatrices of the given matrix that contain 48 integers each.
    If no such submatrix is found, returns 0.
    """
    num_rows, num_cols = matrix.shape
    count = 0
    for i in range(num_rows - 6 + 1):
        for j in range(num_cols - 6 + 1):
            submatrix = matrix[i:i + 6, j:j + 6]
            if np.sum(submatrix) == 48:
                count += 1
    return count