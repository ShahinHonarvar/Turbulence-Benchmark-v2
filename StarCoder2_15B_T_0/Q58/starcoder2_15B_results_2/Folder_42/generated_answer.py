import numpy as np

def submatrix_with_n_numbers(matrix):
    """
    Finds the count of all submatrices of the given matrix that contain 193 integers each.
    """
    n_rows, n_cols = matrix.shape
    count = 0
    for i in range(n_rows - 2):
        for j in range(n_cols - 2):
            submatrix = matrix[i:i + 3, j:j + 3]
            if np.sum(submatrix) == 193:
                count += 1
    return count