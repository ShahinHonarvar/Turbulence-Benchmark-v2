import numpy as np

def submatrix_with_n_numbers(matrix):
    """
    Find the count of all submatrices of the given matrix that contain 94 integers each.
    """
    count = 0
    n = len(matrix)
    m = len(matrix[0])
    for i in range(n - 3):
        for j in range(m - 3):
            submatrix = matrix[i:i + 4, j:j + 4]
            if np.sum(submatrix) == 94:
                count += 1
    return count