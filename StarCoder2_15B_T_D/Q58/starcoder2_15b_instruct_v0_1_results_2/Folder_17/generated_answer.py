import numpy as np

def submatrix_with_n_numbers(matrix):
    """
    Returns the count of all submatrices of the given matrix that contain 166 integers each.
    If no such submatrix is found, the function returns 0.
    """
    num_rows, num_cols = matrix.shape
    count = 0
    for i in range(num_rows - 2):
        for j in range(num_cols - 2):
            submatrix = matrix[i:i + 3, j:j + 3]
            if np.sum(submatrix) == 166:
                count += 1
    return count