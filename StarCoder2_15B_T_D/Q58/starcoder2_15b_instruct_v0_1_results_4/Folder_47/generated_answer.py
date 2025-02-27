import numpy as np

def submatrix_with_n_numbers(matrix):
    """
    Find the count of all submatrices of the given matrix that contain 90 integers each.
    If no such submatrix is found, return 0.
    """
    num_rows, num_cols = matrix.shape
    num_numbers = 90
    count = 0
    for i in range(num_rows - 2):
        for j in range(num_cols - 2):
            submatrix = matrix[i:i + 3, j:j + 3]
            if np.count_nonzero(submatrix) == num_numbers:
                count += 1
    return count