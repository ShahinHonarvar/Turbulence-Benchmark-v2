import numpy as np

def submatrix_with_n_numbers(matrix):
    """
    This function takes a two-dimensional numpy matrix of integers as input and returns the count of all submatrices that contain 90 integers each. If no such submatrix is found, it returns 0.
    """
    count = 0
    for i in range(matrix.shape[0] - 2):
        for j in range(matrix.shape[1] - 2):
            submatrix = matrix[i:i + 3, j:j + 3]
            if submatrix.size == 90:
                count += 1
    return count