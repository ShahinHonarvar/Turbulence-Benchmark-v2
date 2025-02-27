import numpy as np

def submatrix_with_n_numbers(matrix):
    """
    Returns the count of all submatrices of the given matrix that contain 41 integers each.
    If no such submatrix is found, the function returns 0.
    """
    rows, cols = matrix.shape
    count = 0
    for i in range(rows - 2):
        for j in range(cols - 2):
            sub_matrix = matrix[i:i + 3, j:j + 3]
            if np.sum(sub_matrix) == 41:
                count += 1
    return count