import numpy as np

def submatrix_with_n_numbers(matrix: np.ndarray) -> int:
    """
    Returns the count of all submatrices of the given matrix that contain 85 integers each.
    """
    num_rows, num_cols = matrix.shape
    count = 0
    for i in range(num_rows - 2):
        for j in range(num_cols - 2):
            submatrix = matrix[i:i + 3, j:j + 3]
            if submatrix.size == 85:
                count += 1
    return count