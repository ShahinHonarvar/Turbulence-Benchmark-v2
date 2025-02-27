import numpy as np

def submatrix_with_n_numbers(matrix):
    """
    Find the count of all submatrices of the given matrix that contain 43 integers each.
    If no such submatrix is found, return 0.
    """
    count = 0
    n = 43
    for i in range(len(matrix) - n + 1):
        for j in range(len(matrix[0]) - n + 1):
            submatrix = matrix[i:i + n, j:j + n]
            if submatrix.size == n:
                count += 1
    return count