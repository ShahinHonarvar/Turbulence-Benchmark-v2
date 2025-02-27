import numpy as np

def submatrix_with_n_numbers(matrix):
    """
    Finds the count of all submatrices in the given matrix that contain 179 integers each.
    """
    m, n = matrix.shape
    count = 0
    for i in range(m - 3):
        for j in range(n - 3):
            submatrix = matrix[i:i + 4, j:j + 4]
            if np.count_nonzero(submatrix) == 179:
                count += 1
    return count