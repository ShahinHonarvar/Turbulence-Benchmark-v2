import numpy as np

def submatrix_with_n_numbers(matrix):
    """
    Returns the count of all submatrices of the given matrix that contain 10 integers each.
    If no such submatrix is found, the function returns 0.
    """
    n_rows, n_cols = matrix.shape
    count = 0
    for i in range(n_rows - 9):
        for j in range(n_cols - 9):
            submatrix = matrix[i:i + 10, j:j + 10]
            if submatrix.size == 10:
                count += 1
    return count