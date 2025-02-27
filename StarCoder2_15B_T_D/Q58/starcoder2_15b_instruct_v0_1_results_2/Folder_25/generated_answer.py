import numpy as np

def submatrix_with_n_numbers(matrix):
    """
    This function takes a two-dimensional numpy matrix as input and returns the count of
    all submatrices that contain 66 integers each. If no such submatrix is found, it returns 0.
    """
    count = 0
    for i in range(matrix.shape[0] - 2):
        for j in range(matrix.shape[1] - 2):
            submatrix = matrix[i:i + 3, j:j + 3]
            if np.sum(submatrix) == 66:
                count += 1
    return count