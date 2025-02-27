import numpy as np

def submatrix_with_n_numbers(matrix):
    """
    Finds the count of all submatrices of the given matrix that contain 56 integers each.
    """
    num_rows, num_cols = matrix.shape
    count = 0
    for i in range(num_rows - 6):
        for j in range(num_cols - 7):
            submatrix = matrix[i:i + 7, j:j + 8]
            if np.sum(submatrix) == 56:
                count += 1
    return count