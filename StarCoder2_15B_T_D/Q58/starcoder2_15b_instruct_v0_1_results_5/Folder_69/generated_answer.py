import numpy as np

def submatrix_with_n_numbers(matrix):
    """
    This function takes a two-dimensional numpy matrix as input and returns the count of all submatrices
    that contain 126 integers each.
    """
    num_rows, num_cols = matrix.shape
    count = 0
    for i in range(num_rows - 2):
        for j in range(num_cols - 2):
            submatrix = matrix[i:i + 3, j:j + 3]
            if submatrix.size == 126:
                count += 1
    return count