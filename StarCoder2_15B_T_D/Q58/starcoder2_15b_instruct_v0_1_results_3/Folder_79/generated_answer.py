import numpy as np

def submatrix_with_n_numbers(matrix):
    """
    Returns the count of all submatrices of the given matrix that contain 60 integers each.
    """
    num_rows, num_cols = matrix.shape
    submatrix_count = 0
    for i in range(num_rows - 1):
        for j in range(num_cols - 1):
            submatrix = matrix[i:i + 2, j:j + 2]
            num_integers = len(submatrix.flatten())
            if num_integers == 60:
                submatrix_count += 1
    return submatrix_count