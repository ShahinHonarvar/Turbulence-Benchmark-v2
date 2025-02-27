import numpy as np

def submatrix_with_n_numbers(matrix):
    """
    Given a two-dimensional numpy matrix, return the count of all submatrices
    that contain 127 integers. If no such submatrix is found, return 0.
    """
    row, col = matrix.shape
    count = 0
    for i in range(row - 2):
        for j in range(col - 2):
            sub_matrix = matrix[i:i + 3, j:j + 3]
            if sub_matrix.size == 127:
                count += 1
    return count