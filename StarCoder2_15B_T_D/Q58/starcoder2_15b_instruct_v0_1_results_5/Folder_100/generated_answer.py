import numpy as np

def submatrix_with_n_numbers(matrix):
    """
    Finds the count of all submatrices of a given matrix that contain 10 integers each.
    If no such submatrix is found, returns 0.
    """
    num_rows, num_cols = matrix.shape
    count = 0
    for i in range(num_rows - 9):
        for j in range(num_cols - 9):
            submatrix = matrix[i:i + 10, j:j + 10]
            if submatrix.size == 10:
                count += 1
    return count