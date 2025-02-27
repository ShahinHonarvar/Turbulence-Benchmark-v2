import numpy as np

def submatrix_with_n_numbers(matrix):
    """
    This function takes a two-dimensional numpy matrix of integers as input and
    returns the count of all submatrices that contain 66 integers each. If no
    such submatrix is found, the function returns 0.
    """
    count = 0
    n = 66
    for row in range(len(matrix) - n + 1):
        for col in range(len(matrix[0]) - n + 1):
            submatrix = matrix[row:row + n, col:col + n]
            if submatrix.size == n:
                count += 1
    return count