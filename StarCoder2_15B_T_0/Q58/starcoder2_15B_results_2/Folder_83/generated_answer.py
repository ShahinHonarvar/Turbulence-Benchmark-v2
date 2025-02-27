import numpy as np

def submatrix_with_n_numbers(matrix):
    """
    Finds the count of all submatrices of the given matrix that contain 47 integers each.
    If no such submatrix is found, returns 0.
    """
    num_rows, num_cols = matrix.shape
    count = 0
    for i in range(num_rows - 1):
        for j in range(num_cols - 1):
            submatrix = matrix[i:i + 2, j:j + 2]
            if np.sum(submatrix) == 47:
                count += 1
    return count