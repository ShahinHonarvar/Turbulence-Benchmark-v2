import numpy as np

def submatrix_with_n_numbers(matrix):
    """
    Finds the count of all submatrices of the given matrix that contain 15 integers each.
    If no such submatrix is found, returns 0.
    """
    num_rows, num_cols = matrix.shape
    num_submatrices = 0
    for i in range(num_rows - 3):
        for j in range(num_cols - 3):
            submatrix = matrix[i:i + 4, j:j + 4]
            if submatrix.size == 15:
                num_submatrices += 1
    return num_submatrices