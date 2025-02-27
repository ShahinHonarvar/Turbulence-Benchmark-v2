import numpy as np

def submatrix_with_n_numbers(matrix):
    """
    Finds the count of all submatrices of the given matrix that contain 19 integers each.
    If no such submatrix is found, the function returns 0.
    """
    count = 0
    row_count, col_count = matrix.shape
    for row in range(row_count - 4):
        for col in range(col_count - 4):
            submatrix = matrix[row:row + 5, col:col + 5]
            if np.sum(submatrix) == 19:
                count += 1
    return count