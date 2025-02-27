import numpy as np

def submatrix_with_n_numbers(matrix):
    """
    Given a two-dimensional numpy matrix of integers,
    this function returns the count of all submatrices
    that contain exactly 9 integers.
    """
    num_rows, num_cols = matrix.shape
    count = 0
    for row in range(num_rows - 2):
        for col in range(num_cols - 2):
            submatrix = matrix[row:row + 3, col:col + 3]
            if submatrix.size == 9:
                count += 1
    return count