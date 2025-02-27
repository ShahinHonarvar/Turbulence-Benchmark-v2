import numpy as np

def submatrix_with_n_numbers(matrix):
    """
    Finds the count of all submatrices of the given matrix that contain 115 integers each.
    """
    num_submatrices = 0
    for i in range(matrix.shape[0] - 3):
        for j in range(matrix.shape[1] - 3):
            submatrix = matrix[i:i + 4, j:j + 4]
            if np.sum(submatrix) == 115:
                num_submatrices += 1
    return num_submatrices