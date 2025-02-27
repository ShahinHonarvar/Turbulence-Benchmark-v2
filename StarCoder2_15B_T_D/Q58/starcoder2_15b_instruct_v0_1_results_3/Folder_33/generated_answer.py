import numpy as np

def submatrix_with_n_numbers(matrix):
    """
    Finds the count of all submatrices of the given matrix that contain 118 integers each.
    If no such submatrix is found, returns 0.
    """
    count = 0
    rows, cols = matrix.shape
    for i in range(rows - 18 + 1):
        for j in range(cols - 18 + 1):
            submatrix = matrix[i:i + 18, j:j + 18]
            if submatrix.size == 118:
                count += 1
    return count