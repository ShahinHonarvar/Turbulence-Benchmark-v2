import numpy as np

def submatrix_with_n_numbers(matrix):
    """
    Finds the count of all submatrices of the given matrix that contain 175 integers each.
    If no such submatrix is found, returns 0.
    """
    n_rows, n_cols = matrix.shape
    count = 0
    for i in range(n_rows - 4):
        for j in range(n_cols - 4):
            submatrix = matrix[i:i + 5, j:j + 5]
            if submatrix.size == 175:
                count += 1
    return count