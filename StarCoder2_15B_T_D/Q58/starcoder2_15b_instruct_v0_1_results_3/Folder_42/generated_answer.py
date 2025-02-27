import numpy as np

def submatrix_with_n_numbers(matrix):
    """
    Finds the count of all submatrices of the given matrix that contain 193 integers.
    """
    num_submatrices = 0
    for i in range(len(matrix) - 2):
        for j in range(len(matrix[0]) - 2):
            submatrix = matrix[i:i + 3, j:j + 3]
            if np.sum(submatrix) == 193:
                num_submatrices += 1
    return num_submatrices