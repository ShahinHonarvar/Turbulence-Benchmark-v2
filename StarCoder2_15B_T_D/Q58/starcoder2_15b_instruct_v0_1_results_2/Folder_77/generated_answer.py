import numpy as np

def submatrix_with_n_numbers(matrix):
    """
    Finds the count of all submatrices of the given matrix that contain 179 integers each.
    If no such submatrix is found, returns 0.
    """
    num_rows, num_cols = matrix.shape
    count = 0
    for i in range(num_rows - 3):
        for j in range(num_cols - 3):
            submatrix = matrix[i:i + 4, j:j + 4]
            if np.sum(submatrix) == 179:
                count += 1
    return count