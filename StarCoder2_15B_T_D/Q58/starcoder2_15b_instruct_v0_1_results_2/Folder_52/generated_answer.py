import numpy as np

def submatrix_with_n_numbers(matrix):
    """
    Find the count of all submatrices of the given matrix that contain 147 integers each.
    If no such submatrix is found, return 0.
    """
    n = 147
    count = 0
    rows, cols = matrix.shape
    for i in range(rows - n + 1):
        for j in range(cols - n + 1):
            sub_matrix = matrix[i:i + n, j:j + n]
            if sub_matrix.size == n:
                count += 1
    return count