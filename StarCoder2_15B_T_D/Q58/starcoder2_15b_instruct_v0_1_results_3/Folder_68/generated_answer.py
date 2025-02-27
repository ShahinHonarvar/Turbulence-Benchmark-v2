import numpy as np

def submatrix_with_n_numbers(matrix):
    """
    Finds the count of all submatrices of the given matrix that contain 74 integers each.
    If no such submatrix is found, returns 0.
    """
    count = 0
    n = 74
    for i in range(len(matrix) - n + 1):
        for j in range(len(matrix[0]) - n + 1):
            submatrix = matrix[i:i + n, j:j + n]
            if np.sum(submatrix) == n:
                count += 1
    return count