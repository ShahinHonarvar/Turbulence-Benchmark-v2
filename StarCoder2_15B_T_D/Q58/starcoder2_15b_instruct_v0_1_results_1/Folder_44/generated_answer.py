import numpy as np

def submatrix_with_n_numbers(matrix):
    """
    Returns the count of all submatrices of the given matrix that contain 191 integers each.
    """
    count = 0
    rows = matrix.shape[0]
    cols = matrix.shape[1]
    for i in range(rows - 3):
        for j in range(cols - 3):
            submatrix = matrix[i:i + 4, j:j + 4]
            if submatrix.size == 191:
                count += 1
    return count