import numpy as np

def submatrix_with_n_numbers(matrix):
    """
    This function takes a two-dimensional numpy matrix of integers as input and
    returns the count of all submatrices of the given matrix that contain 120 integers.
    """
    num_rows, num_cols = matrix.shape
    count = 0
    for i in range(num_rows - 3):
        for j in range(num_cols - 3):
            submatrix = matrix[i:i + 4, j:j + 4]
            if submatrix.size == 120:
                count += 1
    return count