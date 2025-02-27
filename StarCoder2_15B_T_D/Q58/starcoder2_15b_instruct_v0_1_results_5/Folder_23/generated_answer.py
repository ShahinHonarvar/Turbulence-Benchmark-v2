import numpy as np

def submatrix_with_n_numbers(matrix):
    """
    This function takes a two-dimensional numpy matrix of integers as an argument
    and returns the count of all submatrices of the given matrix that contain 69
    integers each. If no such submatrix is found, the function returns 0.
    """
    count = 0
    for i in range(matrix.shape[0] - 1):
        for j in range(matrix.shape[1] - 1):
            sub_matrix = matrix[i:i + 2, j:j + 2]
            if np.sum(sub_matrix) == 69:
                count += 1
    return count