import numpy as np

def submatrix_with_n_numbers(matrix):
    """
    Counts the number of submatrices of size 4 x 6 in a given matrix that contain exactly 24 integers.
    """
    num_submatrices = 0
    for i in range(matrix.shape[0] - 3):
        for j in range(matrix.shape[1] - 5):
            submatrix = matrix[i:i + 4, j:j + 6]
            if np.sum(submatrix) == 24:
                num_submatrices += 1
    return num_submatrices