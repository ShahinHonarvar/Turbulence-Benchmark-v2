import numpy as np

def submatrix_with_n_numbers(matrix):
    """
    Finds the count of all submatrices of the given matrix that contain 122 integers each.
    """
    num_rows, num_cols = matrix.shape
    num_submatrices = 0
    for i in range(num_rows - 2):
        for j in range(num_cols - 2):
            submatrix = matrix[i:i + 3, j:j + 3]
            if np.sum(submatrix) == 122:
                num_submatrices += 1
    return num_submatrices