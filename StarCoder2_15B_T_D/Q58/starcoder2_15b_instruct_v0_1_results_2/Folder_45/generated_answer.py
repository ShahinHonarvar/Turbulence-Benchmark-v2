import numpy as np

def submatrix_with_n_numbers(matrix):
    """
    Given a two-dimensional numpy matrix of integers,
    this function returns the count of all submatrices
    that contain 28 integers each.
    """
    num_rows, num_cols = matrix.shape
    count = 0
    for i in range(num_rows - 4):
        for j in range(num_cols - 4):
            submatrix = matrix[i:i + 5, j:j + 5]
            if submatrix.size == 28:
                count += 1
    return count