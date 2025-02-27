import numpy as np

def submatrix_with_n_numbers(matrix):
    """
    Find all submatrices of the given matrix that contain 76 integers.
    """
    num_rows, num_cols = matrix.shape
    count = 0
    for i in range(num_rows - 1):
        for j in range(num_cols - 1):
            sub_matrix = matrix[i:i + 2, j:j + 2]
            if sub_matrix.size == 76:
                count += 1
    return count