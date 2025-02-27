import numpy as np

def submatrix_with_n_numbers(matrix):
    """
    Finds the count of all submatrices of the given matrix that contain 8 integers each.
    """
    row_count, col_count = matrix.shape
    submatrix_count = 0
    for i in range(row_count - 2):
        for j in range(col_count - 2):
            submatrix = matrix[i:i + 3, j:j + 3]
            if submatrix.size == 8:
                submatrix_count += 1
    return submatrix_count